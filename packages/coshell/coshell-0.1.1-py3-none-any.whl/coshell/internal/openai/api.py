import os

from typing import Dict


class Api:
    base_url: str = "https://api.openai.com/"
    default_version: str = "v1"
    default_api_key_environment_variable: str = "OPENAI_API_KEY"

    def get_api_key(self) -> str:
        return os.environ.get(self.default_api_key_environment_variable)

    def get_headers(self) -> Dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.get_api_key()}"
        }

    def get_url(self) -> str:
        return f"{self.base_url}{self.default_version}"
