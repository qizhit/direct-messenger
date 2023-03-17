from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI


def api(message: str, apikey: str, webapi: WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)


open_weather = OpenWeather()
# notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

api("Testing the weather: @weather", "7cc3de7bc963865a05395ff953aa1bcf", open_weather)
# expected output should include the original message transcluded
# with the default weather value for the @weather keyword.

api("Testing lastFM: @lastfm", "29f34099931d760c0a78dbfdd6d4ef9f", lastfm)
# expected output include the original message transcluded with the
# default music data assigned to the @lastfm keyword


# zipcode = "92697"
# ccode = "US"
# apikey = "7cc3de7bc963865a05395ff953aa1bcf"
#
# open_weather = OpenWeather(zipcode, ccode)
# open_weather.set_apikey(apikey)
# open_weather.load_data()
#
#
# print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
# print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
# print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
# print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
# print(f"The current weather for {zipcode} is {open_weather.description}")
# print(f"The current humidity for {zipcode} is {open_weather.humidity}")
# print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")


# apikey = "29f34099931d760c0a78dbfdd6d4ef9f"
#
# lastfm = LastFM()
# lastfm.set_apikey(apikey)
# lastfm.load_data()
#
# print(f"The hottest music tag name is {lastfm.tag_name}.")
# print(f"The count of {lastfm.tag_name} is {lastfm.count}")
# print(f"The reach of {lastfm.tag_name} is {lastfm.reach}")
