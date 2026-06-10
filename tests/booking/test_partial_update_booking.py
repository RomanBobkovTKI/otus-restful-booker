import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import CreateBookingResponse, BookingResponse
from utils.data_factory import generate_booking_payload


@pytest.mark.partial_update_booking
def test_partial_update_booking_firstname_lastname(
    booking_client,
    token,
):
    payload = generate_booking_payload()

    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    response = booking_client.partial_update_booking(
        booking_id=created_model.bookingid,
        payload={
            "firstname": "James",
            "lastname": "Brown",
        },
        token=token,
    )

    BookingResponse.model_validate(response)
    BookingAssertions.assert_booking_firstname_and_lastname_updated(
        response=response,
        original_payload=payload,
        expected_firstname="James",
        expected_lastname="Brown",
    )


@pytest.mark.partial_update_booking
def test_partial_update_booking_firstname_only(
    booking_client,
    token,
):
    payload = generate_booking_payload()

    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    response = booking_client.partial_update_booking(
        booking_id=created_model.bookingid,
        payload={
            "firstname": "Ivan",
        },
        token=token,
    )

    BookingResponse.model_validate(response)
    BookingAssertions.assert_booking_firstname_updated(
        response=response,
        original_payload=payload,
        expected_firstname="Ivan",
    )


@pytest.mark.partial_update_booking
@pytest.mark.parametrize(
    "additionalneeds",
    ["Breakfast", "Dinner", "Late checkout", ""],
)
def test_partial_update_booking_additionalneeds(
    booking_client,
    token,
    additionalneeds,
):
    created = booking_client.create_booking(generate_booking_payload())
    created_model = CreateBookingResponse.model_validate(created)

    response = booking_client.partial_update_booking(
        booking_id=created_model.bookingid,
        payload={
            "additionalneeds": additionalneeds,
        },
        token=token,
    )

    BookingResponse.model_validate(response)
    BookingAssertions.assert_booking_additionalneeds_updated(
        response=response,
        expected_additionalneeds=additionalneeds,
    )


@pytest.mark.partial_update_booking
def test_partial_update_booking_persists_changes(
    booking_client,
    token,
):
    payload = generate_booking_payload()

    created = booking_client.create_booking(payload)
    created_model = CreateBookingResponse.model_validate(created)

    booking_client.partial_update_booking(
        booking_id=created_model.bookingid,
        payload={
            "firstname": "James",
        },
        token=token,
    )

    booking = booking_client.get_booking(created_model.bookingid)

    BookingResponse.model_validate(booking)
    BookingAssertions.assert_booking_firstname_equals(
        response=booking,
        expected_firstname="James",
    )


@pytest.mark.partial_update_booking
def test_partial_update_booking_without_token(
    booking_client,
):
    created = booking_client.create_booking(generate_booking_payload())
    created_model = CreateBookingResponse.model_validate(created)

    with pytest.raises(Exception) as exc:
        booking_client.partial_update_booking(
            booking_id=created_model.bookingid,
            payload={
                "firstname": "James",
            },
            token="",
        )

    assert "403" in str(exc.value)
