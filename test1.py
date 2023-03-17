import urllib, json
from urllib import request, error


def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()

    return r_obj


def main() -> None:
    zip = "92697"
    ccode = "US"
    apikey = "7cc3de7bc963865a05395ff953aa1bcf"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        # print(weather_obj['weather'][0]['description'])
        for key, value in weather_obj.items():
            print(key, value)


if __name__ == '__main__':
    main()
