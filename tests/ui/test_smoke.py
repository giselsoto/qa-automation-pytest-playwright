"""Smoke test that proves the browser setup works."""
import pytest
from playwright.sync_api import Page, expect


# Marker: el equivalente a un tag de Behave. Se filtra con: pytest -m smoke
@pytest.mark.smoke
# El nombre de la función es el nombre del test; tiene que empezar con "test_".
# "page" es una fixture de pytest-playwright: el test la pide como parámetro y
# recibe una pestaña del navegador ya abierta, sin crear el driver.
def test_login_page_loads(page: Page) -> None:
    # "/" se completa con --base-url de pyproject.toml.
    page.goto("/")
    # expect() reintenta hasta que se cumple (5 s por defecto), sin WebDriverWait.
    expect(page).to_have_title("Swag Labs")
    # get_by_test_id busca data-test="login-button" (configurado en tests/ui/conftest.py).
    expect(page.get_by_test_id("login-button")).to_be_visible()
