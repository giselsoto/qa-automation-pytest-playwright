"""Page Object for the Sauce Demo products screen."""
from playwright.sync_api import Page


class InventoryPage:
    """Products screen shown after a successful login."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_test_id("title")
        self.items = page.get_by_test_id("inventory-item")
