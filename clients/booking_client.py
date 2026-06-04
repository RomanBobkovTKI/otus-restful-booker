from clients.base_client import BaseClient


class BookingClient(BaseClient):
    BOOKING_PATH = "/booking"

    def get_booking_ids(self, params=None):
        return self.get(self.BOOKING_PATH, params=params)

    def get_booking(self, booking_id: int):
        return self.get(f"{self.BOOKING_PATH}/{booking_id}")

    def create_booking(self, payload: dict):
        return self.post(self.BOOKING_PATH, json=payload)

    def update_booking(self, booking_id: int, payload: dict, token: str):
        headers = {"Cookie": f"token={token}"}

        return self.put(
            f"{self.BOOKING_PATH}/{booking_id}", json=payload, headers=headers
        )

    def partial_update_booking(self, booking_id: int, payload: dict, token: str):
        headers = {"Cookie": f"token={token}"}

        return self.patch(
            f"{self.BOOKING_PATH}/{booking_id}", json=payload, headers=headers
        )

    def delete_booking(self, booking_id: int, token: str):
        headers = {"Cookie": f"token={token}"}

        return self.delete(f"{self.BOOKING_PATH}/{booking_id}", headers=headers)
