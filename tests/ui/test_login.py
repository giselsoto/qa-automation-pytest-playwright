"""UI tests for the Sauce Demo login."""
import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_valid_login(login_page: LoginPage, inventory_page: InventoryPage) -> None:
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items).to_have_count(6)


# Un solo test que corre una vez por cada fila de la lista; "ids" nombra cada caso.
@pytest.mark.parametrize(
    "username, password, error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
    ],
    ids=["locked_user", "wrong_password", "empty_username"],
)
def test_login_errors(login_page: LoginPage, username: str, password: str, error: str) -> None:
    login_page.login(username, password)

    # to_contain_text porque el mensaje real empieza con "Epic sadface: ".
    expect(login_page.error_message).to_contain_text(error)
