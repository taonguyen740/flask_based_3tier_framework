from src.config import Config
# from urllib.parse import urlparse
from src.daos import FactoryInterface
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self, dao_factory: FactoryInterface = None):
        super().__init__(dao_factory)
        self.user_dao = self.dao_factory.create_user_dao()

    def get_user_by_cognito_id(self, cognito_id):
        user = self.user_dao.get_user_by_cognito_id(cognito_id)
        if user:
            permissions = self.user_dao.get_user_permissions(
                user["id"])
            user["permissions"] = [p["code"] for p in permissions]
        return user
