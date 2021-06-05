import os
from src.database import Database, ScopedSession
from src.utils import custom_logging


class BaseDao:
    def __init__(self, *args, **kwargs):
        exclude = []
        self.db = Database()
        self._session = None
        self.is_with_mode = False
        self.commit_required = False
        self.table_name = None
        if "table_name" in kwargs:
            self.table_name = kwargs["table_name"]
        else:
            self.table_name = None
        for attr in dir(self):
            if callable(getattr(self, attr)) and attr[0] != "_" and attr not in exclude:
                if os.environ.get("EXEC_TIME_LOG_ENABLED"):
                    try:
                        setattr(self, attr, custom_logging.exec_time_logging_decorator(
                            getattr(self, attr)))
                    except Exception as e:
                        print(e)

    def __enter__(self):
        self.is_with_mode = True

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type or exc_value or traceback:
                self.session.rollback()
            elif self.commit_required:
                self.session.commit()
        finally:
            self.session.close()
            self._session = None
            self.is_with_mode = False
            self.commit_required = False

    @property
    def session(self) -> ScopedSession:
        if self._session and self.is_with_mode:
            return self._session
        else:
            self._session = self.db.Session()
            return self._session

    def execute_to_dict(self, *args, **kwargs):
        p = self.session.execute(*args, **kwargs)
        res = self.db.to_dict(p)
        return res

    def execute(self, *args, **kwargs):
        p = self.session.execute(*args, **kwargs)
        return p

    def commit(self):
        if not self.is_with_mode:
            try:
                return self.session.commit()
            except Exception as e:
                self.session.rollback()
                raise e
        else:
            # if is_with_mode=True, commit will exec in __exit__()
            self.commit_required = True

    def close(self):
        if not self.is_with_mode:
            self.session.close()
        # with利用する場合、__exit__でcloseする

    def make_bulk_insert_query(self, mapping_data: list, table_name: str = None):
        table_name = table_name or self.table_name
        if type(mapping_data) is not list:
            raise Exception(
                "BaseDao.bulk_insert_mapping: Invalid type of mapping_data. Must be a list if dict")
        values_tuple_lst = []
        for record in mapping_data:
            if type(record) is not dict:
                raise Exception(
                    "BaseDao.bulk_insert_mapping: Invalid type of mapping_data. Must be a list of dict")
            values_tuple_lst.append(tuple(record.values()))
        column_names = ', '.join(list(mapping_data[0].keys()))
        bind_values = ', '.join(
            [f':{column}' for column in list(mapping_data[0].keys())])
        query = f"""INSERT INTO {table_name} ({column_names}) VALUES ({bind_values})"""
        return query

    def bulk_insert_mapping(self, mapping_data: list, table_name: str = None):
        """バルクインサート

        Args:
            mapping_data (list(dict[])): インサートするためのマッピングリスト
            table_name (str): テーブル名

        Returns:
            int: 成功=0

        Examples:
            >>> bulk_insert_mapping([{"project_id": 1, "user_id": 1, "project_id": 1, "user_id": 2}], "T_PROJECT_USERS")
            0
        """
        session = self.db.Session()
        try:
            query = self.make_bulk_insert_query(
                mapping_data, table_name=table_name)
            session.execute(query, mapping_data)
            session.commit()
            return 0
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @staticmethod
    def gen_update_statement(data, prefix=""):
        statements = []
        for key in data.keys():
            if(data[key]):
                stm = "{}{}=:{}".format(prefix, key, key.split('.')[-1])
                statements.append(stm)
        return ', '.join(statements)
