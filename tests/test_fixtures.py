from collections.abc import Iterator

import pytest


@pytest.fixture
def account() -> dict:
    return {"owner": "Gisel", "balance": 1500, "currency": "USD"}


@pytest.fixture(scope="module")
def account_with_cleanup() -> Iterator[dict]:
    print("SETUP: creating account")
    account = {"owner": "Gisel", "balance": 1500, "currency": "USD"}
    yield account
    print("TEARDOWN: deleting account")


def test_account_owner(account: dict) -> None:
    assert account["owner"] == "Gisel"


def test_account_balance(account: dict) -> None:
    assert account["balance"] == 1500


def test_account_owner_with_cleanup(account_with_cleanup: dict) -> None:
    assert account_with_cleanup["owner"] == "Gisel"


def test_account_balance_with_cleanup(account_with_cleanup: dict) -> None:
    assert account_with_cleanup["balance"] == 1500


def test_account_currency_with_cleanup(account_with_cleanup: dict) -> None:
    assert account_with_cleanup["currency"] == "USD"
