from assertions.booking_assertions import BookingAssertions
from models.booking import BookingResponse
from utils.data_factory import generate_booking_payload


def test_create_booking(booking_client):
    payload = generate_booking_payload()
    response = booking_client.create_booking(payload)
    # BookingResponse.model_validate(response)
    # BookingAssertions.assert_booking_matches_payload(response, payload)
