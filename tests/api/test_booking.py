"""API tests for bookings in Restful Booker."""
import requests


# Recibe la reserva ya creada por la fixture; la borra el teardown.
def test_create_booking(api_booking: dict) -> None:
    assert "bookingid" in api_booking
    assert api_booking["booking"]["firstname"] == "Gisel"


# Pide dos fixtures: la URL para el request y la reserva para tener el id.
def test_get_booking(api_base_url: str, api_booking: dict) -> None:
    response = requests.get(
        f"{api_base_url}/booking/{api_booking['bookingid']}",
        headers={"Accept": "application/json"},
        timeout=10,
    )

    assert response.status_code == 200
    assert response.json()["lastname"] == "Soto"


# Caso negativo: sin token la API rechaza el borrado. La reserva queda creada
# y la borra el teardown de la fixture, que sí manda el token.
def test_delete_without_token_is_forbidden(api_base_url: str, api_booking: dict) -> None:
    response = requests.delete(
        f"{api_base_url}/booking/{api_booking['bookingid']}",
        timeout=10,
    )

    assert response.status_code == 403
