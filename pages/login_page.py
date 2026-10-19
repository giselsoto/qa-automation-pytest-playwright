"""Page Object for the Sauce Demo login screen."""
from playwright.sync_api import Page


class LoginPage:
    """Login screen: credentials form and error message."""

    def __init__(self, page: Page) -> None:
        self.page = page
        # Los locators se arman acá porque necesitan "page". Son lazy: no buscan
        # el elemento hasta que se usan, así que crearlos no falla aunque no existan.
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_test_id("error")

    def open(self) -> "LoginPage":
        """Open the login screen."""
        self.page.goto("/")
        # Devuelve el propio objeto para poder encadenar: LoginPage(page).open().login(...)
        return self

    def login(self, username: str, password: str) -> None:
        """Fill in the credentials and submit the form."""
        # fill() y click() esperan solos a que el elemento esté listo (auto-wait).
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
