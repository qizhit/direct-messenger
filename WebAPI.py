"""
Superclass WebAPI
"""

# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950


from abc import ABC, abstractmethod
from urllib import request, error
import json


class WebAPI(ABC):
    """
    Superclass of OpenWeather() and LastFM()
    """

    def __init__(self):
        self.api_key = None

    def _download_url(self, url: str) -> dict:
        """
        Implement web api request code in a way that supports
        all types of web APIs
        """
        response = None

        try:
            response = request.urlopen(url)
            if response.status in [404, 503]:
                raise error.HTTPError

            json_results = response.read()
            r_obj = json.loads(json_results)

        except error.HTTPError:
            raise Exception("\nRemote API is unavailable "
                            "(404 or 503 HTTP response codes)")
        except error.URLError:
            raise Exception("\nLoss of local connection to the Internet")
        except ValueError:
            raise Exception("\nInvalid data formatting from the remote API")

        finally:
            if response is not None:
                response.close()

        return r_obj

    def set_apikey(self, apikey: str) -> None:
        """
        assign aip_key in Superclass
        """
        self.api_key = apikey

    @abstractmethod
    def load_data(self):
        """
        abstract method of OpenWeather and LastFM
        """
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        """
        abstract method of OpenWeather and LastFM
        """
        pass
