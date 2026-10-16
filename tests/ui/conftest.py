"""Fixtures for the UI tests against Sauce Demo."""
# conftest.py: pytest lo carga solo, sin imports, y aplica a los tests de esta
# carpeta y sus subcarpetas. Es el equivalente a environment.py, pero por carpeta.
import pytest
from playwright.sync_api import Playwright


# scope="session": corre una sola vez por corrida.
# autouse=True: se aplica a todos los tests sin que la pidan.
# Recibe la fixture "playwright" del plugin: una fixture puede pedir otras.
@pytest.fixture(scope="session", autouse=True)
def test_id_attribute(playwright: Playwright) -> None:
    # Playwright busca data-testid por defecto; Sauce Demo usa data-test.
    playwright.selectors.set_test_id_attribute("data-test")
