"""API Fixtures"""

from collections.abc import Iterator

import pytest
import requests

NEW_BOOKING = {
    "firstname": "Gisel",
    "lastname": "Soto",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
    "additionalneeds": "Breakfast",
}


@pytest.fixture(scope="session")
def api_base_url() -> str:
    return "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api_token(api_base_url: str) -> str:     # pide la otra fixture como parámetro
    response = requests.post(
        f"{api_base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=10,
    )
    assert response.status_code == 200      # si el login falla, que se vea acá
    return response.json()["token"]


@pytest.fixture
def api_booking(api_base_url: str, api_token: str) -> Iterator[dict]:
    # Setup: crear la reserva.
    response = requests.post(
        f"{api_base_url}/booking",
        json=NEW_BOOKING,
        headers={"Accept": "application/json"},
        timeout=10,
    )
    assert response.status_code == 200
    created = response.json()          # {"bookingid": 1095, "booking": {...}}

    yield created                      # el test recibe esto

    # Teardown: borrar la reserva, aunque el test haya fallado.
    requests.delete(
        f"{api_base_url}/booking/{created['bookingid']}",
        cookies={"token": api_token},
        timeout=10,
    )
