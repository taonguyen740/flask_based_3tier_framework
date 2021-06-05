import pytest
from src.services.division_item_service import DivisionItemService
from src.daos.division_item_dao import RdsDivisionItemDao
from src.services.exceptions import ServiceException, ServiceErrorCode


@pytest.fixture
def perm_svc():
    return DivisionItemService()


divison_items = [
    {
        "code": "STA01",
        "text": "ステータス１"
    },
    {
        "code": "STA02",
        "text": "ステータス２"
    }
]


def mock_get_division_items(self, parrent_code):
    return divison_items


def test_get_division_items_success_case(perm_svc: DivisionItemService, monkeypatch):
    monkeypatch.setattr(RdsDivisionItemDao,
                        "get_division_items", mock_get_division_items)
    res = perm_svc.get_division_items("STATUS")
    assert res == divison_items


def test_get_division_items_invalid_case(perm_svc: DivisionItemService):
    try:
        perm_svc.get_division_items("INVALID")
    except ServiceException as e:
        if e.error == ServiceErrorCode.INVALID_DIVISION_PARRENT_CODE:
            assert True
        else:
            assert False
