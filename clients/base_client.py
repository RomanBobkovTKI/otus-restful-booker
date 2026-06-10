import requests


class BaseClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _request(self, method: str, path: str, **kwargs):
        url = self._url(path)

        response = self.session.request(
            method=method, url=url, timeout=self.timeout, **kwargs
        )

        if not response.ok:
            raise Exception(f"{response.status_code}: {response.text}")

        if not response.text:
            return None

        try:
            return response.json()
        except ValueError:
            return response.text

    def get(self, path: str, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path: str, **kwargs):
        return self._request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs):
        return self._request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs):
        return self._request("DELETE", path, **kwargs)
