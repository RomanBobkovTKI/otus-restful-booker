import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import BookingResponse
from models.booking import CreateBookingResponse
from utils.data_factory import generate_booking_payload


@pytest.mark.update_booking
def test_update_booking(booking_client, token):
    payload = generate_booking_payload()
    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    update_payload = generate_booking_payload()

    response = booking_client.update_booking(
        booking_id=created_model.bookingid,
        payload=update_payload,
        token=token,
    )

    BookingResponse.model_validate(response)
    BookingAssertions.assert_booking_matches_payload(response, update_payload)


@pytest.mark.update_booking
@pytest.mark.parametrize("depositpaid", [True, False])
def test_update_booking_with_depositpaid_values(
    booking_client,
    token,
    depositpaid,
):
    created = booking_client.create_booking(generate_booking_payload())
    created_model = CreateBookingResponse.model_validate(created)

    update_payload = generate_booking_payload()
    update_payload["depositpaid"] = depositpaid

    response = booking_client.update_booking(
        booking_id=created_model.bookingid,
        payload=update_payload,
        token=token,
    )

    BookingResponse.model_validate(response)
    assert response["depositpaid"] == depositpaid


@pytest.mark.update_booking
@pytest.mark.negative
def test_update_booking_without_token(booking_client):
    created = booking_client.create_booking(generate_booking_payload())
    created_model = CreateBookingResponse.model_validate(created)

    update_payload = generate_booking_payload()

    with pytest.raises(Exception) as exc:
        booking_client.update_booking(
            booking_id=created_model.bookingid,
            payload=update_payload,
            token="",
        )

    assert "403" in str(exc.value)
