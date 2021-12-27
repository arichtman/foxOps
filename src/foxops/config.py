# type: ignore
import logging

import requests
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


# NB: This is likely to cause global coupling - rethink
class Config:
    """Structure intended to hold any globally used configuration items"""

    # I think debug can come out of this class - it's only used to set the global logging level...
    def __init__(self, access_token: str, base_url: str, debug: bool = False):
        logging.debug("initializing configuration class")
        self.base_url = base_url
        self.debug = debug
        self.access_token = access_token.strip()
        self.__validate_config()

    # Yuck
    def __str__(self):
        return "\n".join(str(item) for item in [self.base_url, self.debug, self.access_token])

    def __validate_config(self):
        """Checks that the configuration is valid for use"""
        self.__validate_base_url()

    def __validate_base_url(self):
        """Checks that the URL is syntactically correct and accessible"""
        validate_url = URLValidator(schemes=["http", "https"])
        try:
            validate_url(self.base_url)
        except ValidationError:
            return False
        response = requests.get(self.base_url)
        if response.status_code < 400:
            # NB: Select a better exception class
            raise Exception("url provided responded unhealthily (>=400)")

        return True
