import requests

from flask import Flask

app = Flask("weather_api")


def get_weather_data():
    import pprint

    API_URL = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"

    resp = requests.get(API_URL)

    # pprint.pprint(resp.json(), indent=4)

    if resp.status_code == 200:
        if not resp.json().get('dataseries'):
            return None
        return resp.json().get('dataseries')
    else:
        return resp.status_code

@app.route("/")
def weather():
    return get_weather_data()


if __name__ == '__main__':
    # import pprint
    # resp = get_weather_data()

    # pprint.pprint(resp)

    app.run(host="0.0.0.0")