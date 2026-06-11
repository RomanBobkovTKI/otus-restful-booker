import allure
import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import CreateBookingResponse, BookingResponse
from utils.data_factory import generate_booking_payload


@allure.feature("PATCH booking")
@allure.story("Partial update booking")
class TestPartialUpdateBooking:
    @allure.title("Partial update booking firstname and lastname")
    @pytest.mark.partial_update_booking
    def test_partial_update_booking_firstname_lastname(self, booking_client, token):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            created = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Partial update firstname and lastname"):
            response = booking_client.partial_update_booking(
                booking_id=created_model.bookingid,
                payload={
                    "firstname": "James",
                    "lastname": "Brown",
                },
                token=token,
            )

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check firstname and lastname updated"):
            BookingAssertions.assert_booking_firstname_and_lastname_updated(
                response=response,
                original_payload=payload,
                expected_firstname="James",
                expected_lastname="Brown",
            )

    @allure.title("Partial update booking firstname only")
    @pytest.mark.partial_update_booking
    def test_partial_update_booking_firstname_only(self, booking_client, token):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            created = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Partial update firstname"):
            response = booking_client.partial_update_booking(
                booking_id=created_model.bookingid,
                payload={
                    "firstname": "Ivan",
                },
                token=token,
            )

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check firstname updated"):
            BookingAssertions.assert_booking_firstname_updated(
                response=response,
                original_payload=payload,
                expected_firstname="Ivan",
            )

    @allure.title("Partial update booking additionalneeds: {additionalneeds}")
    @pytest.mark.partial_update_booking
    @pytest.mark.parametrize(
        "additionalneeds",
        ["Breakfast", "Dinner", "Late checkout", ""],
    )
    def test_partial_update_booking_additionalneeds(
        self,
        booking_client,
        token,
        additionalneeds,
    ):
        with allure.step("Create booking"):
            created = booking_client.create_booking(generate_booking_payload())

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Partial update additionalneeds"):
            response = booking_client.partial_update_booking(
                booking_id=created_model.bookingid,
                payload={
                    "additionalneeds": additionalneeds,
                },
                token=token,
            )

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check additionalneeds updated"):
            BookingAssertions.assert_booking_additionalneeds_updated(
                response=response,
                expected_additionalneeds=additionalneeds,
            )

    @allure.title("Partial update booking persists changes")
    @pytest.mark.partial_update_booking
    def test_partial_update_booking_persists_changes(self, booking_client, token):
        with allure.step("Generate booking payload"):
            payload = generate_booking_payload()

        with allure.step("Create booking"):
            created = booking_client.create_booking(payload)

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Partial update firstname"):
            booking_client.partial_update_booking(
                booking_id=created_model.bookingid,
                payload={
                    "firstname": "James",
                },
                token=token,
            )

        with allure.step("Get updated booking by id"):
            booking = booking_client.get_booking(created_model.bookingid)

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(booking)

        with allure.step("Check persisted firstname"):
            BookingAssertions.assert_booking_firstname_equals(
                response=booking,
                expected_firstname="James",
            )

    @allure.title("Partial update booking without token")
    @pytest.mark.partial_update_booking
    @pytest.mark.negative
    def test_partial_update_booking_without_token(self, booking_client):
        with allure.step("Create booking"):
            created = booking_client.create_booking(generate_booking_payload())

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Partial update booking without token"):
            with pytest.raises(Exception) as exc:
                booking_client.partial_update_booking(
                    booking_id=created_model.bookingid,
                    payload={
                        "firstname": "James",
                    },
                    token="",
                )

        with allure.step("Check forbidden response"):
            assert "403" in str(exc.value)
