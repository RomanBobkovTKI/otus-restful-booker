import allure
import pytest

from models.booking_id import BookingIdList


@allure.feature("GET bookings id")
@allure.story("Get bookings id")
class TestGetBookingId:
    @allure.title("Get bookings id")
    @pytest.mark.get_booking_id
    def test_get_bookings(self, booking_client):
        with allure.step("Get booking id"):
            response = booking_client.get_booking_ids()

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)

    @allure.title("Get bookings id by firstname")
    @pytest.mark.get_booking_id
    @pytest.mark.parametrize("firstname", ["Eric", "Susan", "Sally"])
    def test_get_bookings_by_firstname(self, booking_client, firstname):
        with allure.step("Get booking id by firstname"):
            response = booking_client.get_booking_ids(params={"firstname": firstname})

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)

    @allure.title("Get bookings id by lastname")
    @pytest.mark.get_booking_id
    @pytest.mark.parametrize("lastname", ["Smith", "Jackson", "Jones"])
    def test_get_bookings_by_lastname(self, booking_client, lastname):
        with allure.step("Get booking id by firstname"):
            response = booking_client.get_booking_ids(params={"lastname": lastname})

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)

    @allure.title("Get bookings id by firstname and lastname")
    @pytest.mark.get_booking_id
    def test_get_booking_by_firstname_and_lastname(self, booking_client):
        with allure.step("Get booking id by firstname and lastname"):
            response = booking_client.get_booking_ids(
                params={"firstname": "Eric", "lastname": "Jackson"}
            )

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)

    @allure.title("Get empty bookings list")
    @pytest.mark.get_booking_id
    def test_search_returns_empty_list_when_no_matches(self, booking_client):
        with allure.step("Get empty bookings list"):
            response = booking_client.get_booking_ids(
                params={"firstname": "ThisNameDoesNotExist123"}
            )

        with allure.step("Validate response"):
            validated = BookingIdList.model_validate(response)

        with allure.step("List is empty"):
            assert validated.root == []

    @allure.title("Get bookings id by checkin")
    @pytest.mark.get_booking_id
    @pytest.mark.parametrize("checkin", ["2019-12-17", "2015-02-02", "2025-01-20"])
    def test_get_bookings_by_checkin(self, booking_client, checkin):
        with allure.step("Get booking id by checkin"):
            response = booking_client.get_booking_ids(params={"checkin": checkin})

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)

    @allure.title("Get bookings id by checkout")
    @pytest.mark.get_booking_id
    @pytest.mark.parametrize("checkout", ["2025-03-19", "2021-11-14", "2024-03-02"])
    def test_get_bookings_by_checkout(self, booking_client, checkout):
        with allure.step("Get booking id by checkout"):
            response = booking_client.get_booking_ids(params={"checkout": checkout})

        with allure.step("Validate response"):
            BookingIdList.model_validate(response)
