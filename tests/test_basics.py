
def test_upper() -> None:
    assert "hello".upper() == "HELLO"


def test_tool_in_list() -> None:
    tool = "Playwright"
    tools = ["Selenium", "Playwright", "Cypress"]
    assert tool in tools


def test_account_matches() -> None:
    expected = {"owner": "Gisel", "balance": 1500, "currency": "USD"}
    actual = {"owner": "Gisel", "balance": 1500, "currency": "USD"}
    assert expected == actual
