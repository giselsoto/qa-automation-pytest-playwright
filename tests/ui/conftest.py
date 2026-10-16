"""Fixtures for the UI tests against Sauce Demo."""
import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session", autouse=True)
def test_id_attribute(playwright: Playwright) -> None:
    # Sauce Demo marks its elements with data-test instead of data-testid
    playwright.selectors.set_test_id_attribute("data-test")
