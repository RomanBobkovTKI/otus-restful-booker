from datetime import date, timedelta

from faker import Faker

fake = Faker()


def generate_booking_payload():
    checkin = fake.date_between(start_date="+1d", end_date="+30d")

    checkout = checkin + timedelta(days=fake.random_int(1, 14))

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(50, 1000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
        },
        "additionalneeds": fake.random_element(
            elements=("Breakfast", "Lunch", "Dinner", "Late Checkout", "Baby Crib")
        ),
    }
