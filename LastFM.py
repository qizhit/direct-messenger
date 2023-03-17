"""
Module for LastFM API：

I choose the API method called "tag.getTopTags".

The link is https://www.last.fm/api/show/tag.getTopTags

My key is 29f34099931d760c0a78dbfdd6d4ef9f

The url with my key is https://ws.audioscrobbler.com/2.0/?method=
tag.getTopTags&api_key=29f34099931d760c0a78dbfdd6d4ef9f&format=json

This API method shows rankings of music genres.

My code focus on the top music genre, rock, and can
replace the keyword @lastfm to rock.
"""

# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Qizhi Tian
# qizhit@uci.edu
# 45765950

# API key	29f34099931d760c0a78dbfdd6d4ef9f

from WebAPI import WebAPI


class LastFM(WebAPI):
    """
    LastFM API class
    """
    def __init__(self):
        super().__init__()
        self.tag_name = ""
        self.count = ""
        self.reach = ""

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
        url = f"http://ws.audioscrobbler.com/2.0/?method=" \
              f"tag.getTopTags&api_key={self.api_key}&format=json"
        try:
            r_obj = self._download_url(url)
        except Exception as e:
            print(e)
        else:
            self.tag_name = r_obj["toptags"]["tag"][0]["name"]
            self.count = r_obj["toptags"]["tag"][0]["count"]
            self.reach = r_obj["toptags"]["tag"][0]["reach"]

    def transclude(self, message: str) -> str:
        """
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude

        :returns: The transcluded message
        """
        if "@lastfm" in message:
            message = message.replace("@lastfm", self.tag_name)
        return message
