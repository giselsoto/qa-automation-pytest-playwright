"""Fixtures for the UI tests against Sauce Demo."""
# conftest.py: pytest lo carga solo, sin imports, y aplica a los tests de esta
# carpeta y sus subcarpetas. Es el equivalente a environment.py, pero por carpeta.
import pytest
from playwright.sync_api import Page, Playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# scope="session": corre una sola vez por corrida.
# autouse=True: se aplica a todos los tests sin que la pidan.
# Recibe la fixture "playwright" del plugin: una fixture puede pedir otras.
@pytest.fixture(scope="session", autouse=True)
def test_id_attribute(playwright: Playwright) -> None:
    # Playwright busca data-testid por defecto; Sauce Demo usa data-test.
    playwright.selectors.set_test_id_attribute("data-test")


# Entrega la pantalla de login ya abierta. El test la pide en lugar de "page".
@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page).open()


# Usa la misma "page" que login_page: pytest crea una sola por test.
@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)
