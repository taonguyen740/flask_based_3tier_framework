import json
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
import traceback
from flask import request
from flask_restful import HTTPException
import flask_restful
from functools import wraps
import jwt
from src.constants import SystemGroupName
from src.services import UserService
from src.daos import ProductionFactory
from ..errors import errors

from webargs.flaskparser import parser


@parser.error_handler
def handle_error(error, req, schema, *, error_status_code, error_headers):
    raise error


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = None
        auth_headers = request.headers.get("Authorization", "").split()
        try:
            if len(auth_headers) != 2:
                raise errors.HTTPTokenRequired
            token = auth_headers[1]
            data = jwt.decode(token, verify=False)
            cognito_id = data["sub"]
            email = data["email"]
            groups = data.get("cognito:groups") or []
            if SystemGroupName.USER_GROUP_NAME in groups or SystemGroupName.ADMIN_GROUP_NAME in groups:
                user_svc = UserService(ProductionFactory())
                user = user_svc.get_user_by_cognito_id(cognito_id)
                if not user:
                    raise errors.HTTPInvalidTokenError
                else:
                    user_id = user["id"]
            else:
                raise errors.HTTPPermissionDenied
            auth_data = {
                "email": email,
                "user_id": user_id,
                "cognito_id": cognito_id,
                "groups": groups,
                "permissions": user["permissions"]
            }
            return func(auth_data, *args, **kwargs)
        except jwt.ExpiredSignatureError as e:
            raise errors.HTTPExpiredSignatureError
        except jwt.InvalidTokenError as e:
            raise errors.HTTPInvalidTokenError
        except HTTPException as e:
            traceback.print_exc()
            raise e
        except ValidationError as e:
            traceback.print_exc()
            raise errors.HTTPBadRequest(custom_message=json.dumps(str(e)))
        except Exception as e:
            traceback.print_exc()
            raise errors.HTTPServerError
    return wrapper


class BaseController(flask_restful.Resource):
    method_decorators = [token_required]  # applies to all inherited resources

    def __init__(self, *args, **kwargs):
        super().__init__()
