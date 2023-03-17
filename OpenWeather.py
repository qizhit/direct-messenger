"""
Module for OpenWeather API
"""

# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950

# API key: 7cc3de7bc963865a05395ff953aa1bcf

from WebAPI import WebAPI


class OpenWeather(WebAPI):
    """
    OpenWeather API class
    """
    def __init__(self, zip_code="92697", c_code="US"):
        super().__init__()
        self.zip_code = str(zip_code)
        self.c_code = str(c_code)
        self.temperature = ""
        self.high_temperature = ""
        self.low_temperature = ""
        self.longitude = ""
        self.latitude = ""
        self.description = ""
        self.humidity = ""
        self.city = ""
        self.sunset = ""

    def set_apikey(self, apikey: str) -> None:
        """
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        """
        super().set_apikey(apikey)

    def load_data(self) -> None:
        """
        Calls the web api using the required values and stores the
        response in class data attributes.
        """
        url = f"http://api.openweathermap.org/data/2.5/weather?zip=" \
              f"{self.zip_code},{self.c_code}&appid={self.api_key}"

        try:
            r_obj = self._download_url(url)
        except Exception as e:
            print(e)
        else:
            self.temperature = r_obj['main']['temp']
            self.high_temperature = r_obj['main']['temp_max']
            self.low_temperature = r_obj['main']['temp_min']
            self.longitude = r_obj['coord']['lon']
            self.latitude = r_obj['coord']['lat']
            self.description = r_obj['weather'][0]['description']
            self.humidity = r_obj['main']['humidity']
            self.city = r_obj['name']
            self.sunset = r_obj['sys']['sunset']

    def transclude(self, message: str) -> str:
        """
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        """
        if "@weather" in message:
            message = message.replace("@weather", self.description)
        return message
