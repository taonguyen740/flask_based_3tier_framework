from . import UserDaoInterface
from ..base_dao import BaseDao
from sqlalchemy import text, bindparam

SECRET_KEY = b"XNKVy8J8UZWZhK3t5kiejdA3JH8oXJGRpBEVF9RbcRA="


class RdsUserDao(UserDaoInterface, BaseDao):
    def get_user_by_cognito_id(self, cognito_id):
        try:
            query = """
            SELECT U.id,U.email,U.cognito_id
            FROM M_USERS
            WHERE cognito_id=:cognito_id
            """
            results = self.execute_to_dict(query, {"cognito_id": cognito_id})
            if results:
                user = results[0]
                return user
            return None
        finally:
            self.close()

    def get_user_permissions(self, user_id):
        try:
            query = """
            SELECT  DISTINCT P.code
            FROM T_USER_ROLES R LEFT JOIN M_PERMISSIONS P ON R.id=P.role_id
            WHERE R.user_id=:user_id
            """
            results = self.execute_to_dict(query, {"user_id": user_id})
            return results
        finally:
            self.close()
