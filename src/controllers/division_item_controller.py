from marshmallow import EXCLUDE
from .base_controller import BaseController
from .schemas.division_item_schema import DivisionItemSchema
from src.services import DivisionItemService
from src.services.exceptions import ServiceException, ServiceErrorCode
from .errors import errors


class DivisionItemController(BaseController):
    def __init__(self):
        super().__init__()
        self.division_item_svc = DivisionItemService()

    def get(self, auth_data, parent_code):
        """
        @api {get} /division_item/:parent_code 区分項目取得API
        @apiName GetDivisionItem
        @apiGroup DivisionItem
        @apiPermission GetDivisionItem
        @apiParam {String}  parent_code 親区分コード.

        @apiSuccess {Object[]} divisionItem 区分項目.
        @apiSuccess {Number} divisionItem.code  区分コード.
        @apiSuccess {String} divisionItem.text  区分テキスト.
        @apiSuccessExample {json}  Success-Response:
            HTTP/1.1 200 OK
            [
                {
                    "code": "STA01",
                    "text": "ステータス１"
                },
                {
                    "code": "STA02",
                    "text": "ステータス２"
                }
            ]
        @apiError InternalServerError サーバーエラー.
        @apiErrorExample Error-Response:
            HTTP/1.1 500 Internal Server Error
            {
                'message': 'Server Error.',
                'status': 500,
                'code': 'BAS_5000'
            }
        """
        try:
            res = self.division_item_svc.get_division_items(parent_code)

            return DivisionItemSchema(many=True).load(res, unknown=EXCLUDE)

        except ServiceException as e:
            if e.error == ServiceErrorCode.INVALID_DIVISION_PARRENT_CODE:
                raise errors.HTTPParentCodeNotFound
            else:
                raise e
