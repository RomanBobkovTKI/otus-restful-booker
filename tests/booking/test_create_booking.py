import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import CreateBookingResponse, BookingResponse
from utils.data_factory import generate_booking_payload


@pytest.mark.create_booking
def test_create_booking(booking_client):
    payload = generate_booking_payload()

    response = booking_client.create_booking(payload)

    CreateBookingResponse.model_validate(response)
    BookingAssertions.assert_created_booking_matches_payload(response, payload)


@pytest.mark.create_booking
def test_created_booking_can_be_retrieved_by_id(booking_client):
    payload = generate_booking_payload()

    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    response = booking_client.get_booking(created_model.bookingid)

    BookingResponse.model_validate(response)
    BookingAssertions.assert_booking_matches_payload(response, payload)


@pytest.mark.create_booking
def test_create_booking_with_empty_payload(booking_client):
    with pytest.raises(Exception) as exc:
        booking_client.create_booking({})

    assert "500" in str(exc.value) or "400" in str(exc.value)
