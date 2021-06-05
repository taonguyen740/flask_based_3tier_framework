from flask_restful import HTTPException


class BaseHTTPException(HTTPException):
    def __init__(self, api_code=None, custom_message=None):
        super().__init__()
        self.api_code = api_code
        self.custom_message = custom_message


class HTTPTokenRequired(BaseHTTPException):
    pass


class HTTPPermissionDenied(BaseHTTPException):
    pass


class HTTPServerError(BaseHTTPException):
    pass


class HTTPExpiredSignatureError(BaseHTTPException):
    pass


class HTTPInvalidTokenError(BaseHTTPException):
    pass


class HTTPInvalidMediaImage(BaseHTTPException):
    pass


class HTTPInvalidInputData(BaseHTTPException):
    pass


class HTTPProjectNameTaken(BaseHTTPException):
    pass


class HTTPInvalidCreativeBoxUrl(BaseHTTPException):
    pass


class HTTPBaseDesignNotFoundError(BaseHTTPException):
    pass


class HTTPParentCodeNotFound(BaseHTTPException):
    pass


class HTTPInvalidMenuCode(BaseHTTPException):
    pass


class HTTPBadRequest(BaseHTTPException):
    pass


class HTTPInvalidAssignStatus(BaseHTTPException):
    pass


class HTTPInvalidCommentTo(BaseHTTPException):
    pass


class HTTPSlackOauthError(BaseHTTPException):
    pass


class HTTPNotInChannel(BaseHTTPException):
    pass


class HTTPClientNameTaken(BaseHTTPException):
    pass


class HTTPStructureNameTaken(BaseHTTPException):
    pass


class HTTPStructureCodeTaken(BaseHTTPException):
    pass


class HTTPInvalidBreadCrumbTypeError(BaseHTTPException):
    pass


class HTTPClientNotFoundError(BaseHTTPException):
    pass


class HTTPClientProjectIdSpaceIsFull(BaseHTTPException):
    pass


class HTTPProjectNotFound(BaseHTTPException):
    pass


class HTTPSystemMediaItemDuplicated(BaseHTTPException):
    pass


errors = {
    'HTTPServerError': {
        'message': 'Server Error.',
        'status': 500,
        'code': 'BAS.WA5000'
    },
    'HTTPBadRequest': {
        'message': 'Bad Request.',
        'status': 400,
        'code': 'BAS.WA4000'
    },
    'HTTPTokenRequired': {
        'message': 'Token required.',
        'status': 400,
        'code': 'BAS.WA4001'
    },
    'HTTPExpiredSignatureError': {
        'message': 'ExpiredSignatureError.',
        'status': 400,
        'code': 'BAS.WA4003'
    },
    'HTTPInvalidTokenError': {
        'message': 'InvalidTokenError.',
        'status': 400,
        'code': 'BAS.WA4004'
    },
    'HTTPPermissionDenied': {
        'message': 'You don\'t have permission to access this resource.',
        'status': 400,
        'code': 'BAS.WA4002'
    },
    'HTTPInvalidAssignStatus': {
        'message': 'Invalid assign status.',
        'status': 400,
        'code': 'F23.WA6001'
    },
    'HTTPInvalidMediaImage': {
        'message': 'The upload file is invalid by media regulation',
        'status': 400,
        'code': 'F25.WA6002'
    },
    'HTTPProjectNameTaken': {
        'message': 'Project name taken.',
        'status': 400,
        'code': 'F26.WA6003'
    },
    'HTTPInvalidCreativeBoxUrl': {
        'message': 'Invalid creative box url.',
        'status': 400,
        'code': 'F26.WA6004'
    },
    'HTTPBaseDesignNotFoundError': {
        'message': 'Base design not found',
        'status': 400,
        'code': 'F38.WA6005'
    },
    'HTTPParentCodeNotFound': {
        'message': 'Parent Code Not Found.',
        'status': 400,
        'code': 'F40.WA4005'
    },
    'HTTPInvalidMenuCode': {
        'message': 'Invalid menu code, must one of ("PRJ", "CLI") .',
        'status': 400,
        'code': 'F43.WA4006'
    },
    'HTTPInvalidCommentTo': {
        'message': 'Invalid comment path!',
        'status': 400,
        'code': 'WA4007'
    },
    'HTTPSlackOauthError': {
        'message': 'Slack Oauth fail!',
        'status': 400,
        'code': 'WA4008'
    },
    'HTTPNotInChannel': {
        'message': 'User not in channel!',
        'status': 400,
        'code': 'WA4009'
    },
    'HTTPClientNameTaken': {
        'message': 'Client name taken.',
        'status': 400,
        'code': 'WA4010'
    },
    'HTTPStructureNameTaken': {
        'message': 'Structure name taken.',
        'status': 400,
        'code': 'WA4011'
    },
    'HTTPStructureCodeTaken': {
        'message': 'Structure code taken.',
        'status': 400,
        'code': 'WA4012'
    },
    'HTTPInvalidBreadCrumbError': {
        'message': 'Invalid breadcrumb type',
        'status': 400,
        'code': 'WA4013'
    },
    'HTTPClientNotFoundError': {
        'message': 'Client Not Found',
        'status': '404',
        'code': 'WA4014'
    },
    'HTTPClientProjectIdSpaceIsFull': {
        'message': 'Client ProjectId Space Is Full',
        'status': 400,
        'code': 'WA4015'
    },
    'HTTPProjectNotFound': {
        'message': 'Project Not Found',
        'status': 404,
        'code': 'WA4016'
    },
    'HTTPSystemMediaItemDuplicated': {
        'message': 'System Media Code is duplicated',
        'status': 404,
        'code': 'WA4017'
    }
}
