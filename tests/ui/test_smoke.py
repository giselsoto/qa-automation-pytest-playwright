"""Smoke test that proves the browser setup works."""
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_login_page_loads(page: Page) -> None:
    page.goto("/")
    expect(page).to_have_title("Swag Labs")
    expect(page.get_by_test_id("login-button")).to_be_visible()
