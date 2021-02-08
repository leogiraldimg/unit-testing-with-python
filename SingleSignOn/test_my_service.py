from unittest.mock import Mock

from my_service import MyService, Request
from single_sign_on import SSOToken, SingleSignOnRegistry

def test_hello_game():
    stub_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(stub_sso_registry)
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"

def test_single_sign_on():
    spy_sso_registry = Mock(SingleSignOnRegistry)
    service = MyService(spy_sso_registry)
    token = SSOToken
    service.handle(Request("Emily"), token)
    spy_sso_registry.is_valid.assert_called_with(token)