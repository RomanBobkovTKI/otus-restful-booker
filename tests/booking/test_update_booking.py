import allure
import pytest

from assertions.booking_assertions import BookingAssertions
from models.booking import BookingResponse, CreateBookingResponse
from utils.data_factory import generate_booking_payload


@allure.feature("PUT booking")
@allure.story("Update booking")
class TestUpdateBooking:
    @allure.title("Update booking")
    @pytest.mark.update_booking
    def test_update_booking(self, booking_client, token):
        with allure.step("Create booking"):
            created = booking_client.create_booking(generate_booking_payload())

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Generate update booking payload"):
            update_payload = generate_booking_payload()

        with allure.step("Update booking"):
            response = booking_client.update_booking(
                booking_id=created_model.bookingid,
                payload=update_payload,
                token=token,
            )

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check updated booking matches payload"):
            BookingAssertions.assert_booking_matches_payload(
                response,
                update_payload,
            )

    @allure.title("Update booking with depositpaid: {depositpaid}")
    @pytest.mark.update_booking
    @pytest.mark.parametrize("depositpaid", [True, False])
    def test_update_booking_with_depositpaid_values(
        self,
        booking_client,
        token,
        depositpaid,
    ):
        with allure.step("Create booking"):
            created = booking_client.create_booking(generate_booking_payload())

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Generate update booking payload"):
            update_payload = generate_booking_payload()
            update_payload["depositpaid"] = depositpaid

        with allure.step("Update booking"):
            response = booking_client.update_booking(
                booking_id=created_model.bookingid,
                payload=update_payload,
                token=token,
            )

        with allure.step("Validate booking response schema"):
            BookingResponse.model_validate(response)

        with allure.step("Check depositpaid value"):
            assert response["depositpaid"] == depositpaid

    @allure.title("Update booking without token")
    @pytest.mark.update_booking
    @pytest.mark.negative
    def test_update_booking_without_token(self, booking_client):
        with allure.step("Create booking"):
            created = booking_client.create_booking(generate_booking_payload())

        with allure.step("Validate create booking response schema"):
            created_model = CreateBookingResponse.model_validate(created)

        with allure.step("Generate update booking payload"):
            update_payload = generate_booking_payload()

        with allure.step("Update booking without token"):
            with pytest.raises(Exception) as exc:
                booking_client.update_booking(
                    booking_id=created_model.bookingid,
                    payload=update_payload,
                    token="",
                )

        with allure.step("Check forbidden response"):
            assert "403" in str(exc.value)
