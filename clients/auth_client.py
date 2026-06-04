from clients.base_client import BaseClient


class AuthClient(BaseClient):
    AUTH_PATH = "/auth"

    def get_token(self, username: str, password: str) -> str:
        payload = {"username": username, "password": password}

        response = self.post(self.AUTH_PATH, json=payload)

        return response["token"]
