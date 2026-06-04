def test_create_booking(booking_client):
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-10"},
        "additionalneeds": "Breakfast",
    }

    response = booking_client.create_booking(payload)

    assert "bookingid" in response
    assert response["booking"]["firstname"] == "John"
