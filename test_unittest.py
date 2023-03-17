"""
unit_test: test OpenWeather() and LastFM()
"""

# Qizhi Tian
# qizhit@uci.edu
# 45765950

import unittest
from urllib import request
import json
from OpenWeather import OpenWeather
from LastFM import LastFM


def api(message: str, apikey: str, webapi):
    """
    call webapi
    """
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    return result


class TestAPI(unittest.TestCase):
    """
    Test OpenWeather() and LastFM()
    """
    def test_openweather(self):
        """
        test OpenWeather
        """
        # Organize Phrase
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" \
              "92697,US&appid=7cc3de7bc963865a05395ff953aa1bcf"
        with request.urlopen(url) as response:
            json_results = response.read()
            r_obj = json.loads(json_results)
            description = r_obj['weather'][0]['description']

        message = "Testing the weather: @weather"
        new = message.replace("@weather", description)
        # Action Phrase
        open_weather = OpenWeather()
        result = api("Testing the weather: @weather",
                     "7cc3de7bc963865a05395ff953aa1bcf", open_weather)
        # Assert Phrase
        assert new == result

    def test_lastfm(self):
        """
        test LastFM
        """
        url = "http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&" \
              "api_key=29f34099931d760c0a78dbfdd6d4ef9f&format=json"
        with request.urlopen(url) as response:
            json_results = response.read()
            r_obj = json.loads(json_results)
            tag_name = r_obj["toptags"]["tag"][0]["name"]

        message = "Testing lastFM: @lastfm"
        new = message.replace("@lastfm", tag_name)
        # Action Phrase
        lastfm = LastFM()
        result = api("Testing lastFM: @lastfm",
                     "29f34099931d760c0a78dbfdd6d4ef9f", lastfm)
        # Assert Phrase
        assert new == result


if __name__ == "__main__":
    unittest.main()
