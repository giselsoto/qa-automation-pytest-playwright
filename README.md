# QA Automation with Pytest and Playwright

Test automation project in Python: UI tests with Playwright and API tests with requests, both run with Pytest.

- **UI:** [Sauce Demo](https://www.saucedemo.com), a practice e-commerce site.
- **API:** [Restful Booker](https://restful-booker.herokuapp.com), a practice booking API.

## Stack

- Python 3.12
- Pytest
- Playwright (`pytest-playwright`)
- requests

## Project structure

```
pages/          Page Objects, one per screen
tests/
  conftest.py   Shared fixtures
  api/          API tests
  ui/           UI tests
pyproject.toml  Pytest configuration (base URL, markers)
```

## Getting started

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
playwright install chromium
```

## Running the tests

```bash
pytest                          # all tests, headless
pytest -m smoke                 # only smoke tests
pytest --headed --slowmo 500    # watch the browser
pytest --browser firefox        # another browser
```

## Roadmap

- [x] Project setup and smoke test
- [x] API tests with fixtures for setup and teardown
- [x] Page Objects and UI tests for login
- [x] Parametrized negative cases
- [ ] UI tests for cart and checkout
- [ ] CI with GitHub Actions and test reports
