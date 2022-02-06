# type: ignore
import logging

import requests
from django.core.validators import URLValidator


# NB: This is likely to cause global coupling - rethink
class Config:
    """Structure intended to hold any globally used configuration items"""

    def __init__(self, access_token: str, base_url: str):
        logging.debug("initializing configuration class")
        self.base_url = base_url
        self.access_token = access_token.strip()
        self.__validate_config()

    # Yuck
    def __str__(self):
        return "\n".join(str(item) for item in [self.base_url, self.access_token])

    # I think this indirection will fall to YAGNI
    def __validate_config(self) -> None:
        """Checks that the configuration is valid for use"""
        self.__validate_base_url()

    def __validate_base_url(self) -> None:
        """Checks that the URL is syntactically correct and accessible"""
        validate_url = URLValidator(schemes=["http", "https"])
        validate_url(self.base_url)
        response = requests.get(self.base_url)
        if response.status_code >= 400:
            # NB: Select a better exception class
            raise Exception("URL provided responded unhealthily (>=400)")
