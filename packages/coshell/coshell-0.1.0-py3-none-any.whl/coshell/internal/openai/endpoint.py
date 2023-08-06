from typing import Any, Dict

import requests

from coshell.internal.openai.api import Api


class Endpoint:

    def __init__(self, api: Api, endpoint: str):
        self.api: Api = api
        self.endpoint: str = endpoint

    def get_url(self) -> str:
        return f"{self.api.get_url()}/{self.endpoint}"

    def post(self, data: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(self.get_url(), headers=self.api.get_headers(), json=data)
        if response.status_code >= 300:
            print(response.status_code)
            print(response.reason)
            print(response.json())
            response.raise_for_status()
        return response.json()
