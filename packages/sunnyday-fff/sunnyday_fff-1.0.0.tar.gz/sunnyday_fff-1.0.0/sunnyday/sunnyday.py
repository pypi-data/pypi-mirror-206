
import requests
from pprint import pprint


class Weather:

    """
    Creates a Weather object getting an API key as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # The API key below is not guaranteed to work.
    # Get your own API key from https://openweathermap.org
    # You need to wait a couple of hours for the API key to be activated.

    # Using a city name:
    >>> weather_a = Weather(api_key="fff2c6c297eb8f562cbf3929180bb604", city="London")

    # Using latitude and longitude coordinates:
    >>> weather_b = Weather(api_key="fff2c6c297eb8f562cbf3929180bb604", lat=41.1, lon=-4.1)

    # Change units (from default units which are metric to imperial):
    >>> weather_c = Weather(api_key="fff2c6c297eb8f562cbf3929180bb604", city="Tokyo", units="imperial")

    # Get complete weather data for the next 12 hours:
    >>> weather_a.next_12h()

    # Get simplified weather data for the next 12 hours:
    >>> weather_a.next_12h_simplified()

    # Get complete weather data for the next 24 hours:
    >>> weather_b.next_24h()

    # Get simplified weather data for the next 24 hours:
    >>> weather_b.next_24h_simplified()

    # At the bottom of this file you can find examples/practice of all instances with this package.
    # Have fun :-)
    """

    def __init__(self, city=None, lat=None, lon=None,
                 api_key="fff2c6c297eb8f562cbf3929180bb604", units="metric"):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?" \
                  f"q={city}" \
                  f"&appid={api_key}" \
                  f"&units={units}"
            response = requests.get(url)
            self.data = response.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?" \
                  f"lat={lat}"\
                  f"&lon={lon}"\
                  f"&appid={api_key}" \
                  f"&units={units}"
            response = requests.get(url)
            self.data = response.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments.")
        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
        Returns complete weather data every 3 hours
        for the next 12 hours as a list of dicts.
        """
        return self.data['list'][:4]

    def next_24h(self):
        """
        Returns complete weather data every 3 hours
        for the next 24 hours as a list of dicts.
        """
        return self.data['list'][:8]

    def next_12h_simplified(self):
        """
        Returns date, temperature and sky condition every 3 hours
        for the next 12 hours as a list of tuples.
        """
        simple_data = []
        for i in self.data['list'][:4]:
            simple_data.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description']))
        return simple_data

    def next_24h_simplified(self):
        """
        Returns date, temperature and sky condition every 3 hours
        for the next 24 hours as a list of tuples.
        """
        simple_data = []
        for i in self.data['list'][:8]:
            simple_data.append((i['dt_txt'], i['main']['temp'], i['weather'][0]['description']))
        return simple_data


if __name__ == "__main__":

    #  * Next 12h by city
    weather1 = Weather(city="Split")
    # pprint(weather1.next_12h())

    # * Simplified practice
    next_12h_simple = weather1.next_12h_simplified()
    print(next_12h_simple)
    print(next_12h_simple[0])
    print(next_12h_simple[0][0])

    #  * Next 24h
    # pprint(weather1.next_24h_simplified())
    # pprint(weather1.next_24h())

    #  * By lat and lon
    # weather2 = Weather(lat=4.1, lon=3.2)
    # print(weather2.next_12h())

    #  * Change units
    # weather3 = Weather(city="Tokyo", units="imperial")
    # print(weather3.next_12h())

    #  * Priority is on the city
    # weather4 = Weather(city="Split", lat=4.1, lon=3.2)
    # print(weather4.next_12h())

    #  * Raise a type error
    # weather5 = Weather(None)
    # weather5.next_12h()

    #  * Raise a value error
    # weather6 = Weather(city="asgshsdhjd")
    # weather6.next_12h()
