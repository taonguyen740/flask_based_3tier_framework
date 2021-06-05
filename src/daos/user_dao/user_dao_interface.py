from abc import ABC, abstractmethod


class UserDaoInterface(ABC):
    @abstractmethod
    def get_user_by_cognito_id(self, cognito_id):
        """CognitoIdによりユーザー情報をGetする

        Args:
            cognito_id (int): CognitoでのユーザーID

        Returns:
            dict[int, str, str, str]) or None: ユーザー情報

        Examples:
            >>> get_user_by_cognito_id("COGNITO_ID_01")
                {
                    "id": 1,
                    "cognito_id": "COGNITO_ID_01",
                    "email": "dinhtao995@gmail.com",
                    "fullname": "タオグエン"
                }
        """
        raise NotImplementedError

    @abstractmethod
    def get_user_permissions(self, user_id):
        """User Idによりユーザー権限一覧をGetする

        Args:
            user_id (int): ユーザーID

        Returns:
            list(dict[str])): ユーザー権限リスト

        Examples:
            >>> get_user_permissions(1)
                [
                    {
                        "code": "P001"
                    },
                    {
                        "code": "P002"
                    }
                ]
        """
        raise NotImplementedError
