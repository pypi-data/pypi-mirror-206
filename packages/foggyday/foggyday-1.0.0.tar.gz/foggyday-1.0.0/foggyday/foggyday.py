import requests


class Weather:
    """
    Creates a Weather object getting an apikey as input and either a city name or lat and lon coordinates.

    Package use example:

    # Creates a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own api key from https://openweathermap.org
    # And wait a couple of hours for the api key to be activated

    >>> weather1 = Weather(apikey='341cddee0d757d3bfdff39f67b120f3c', city='Moscow')

    # Using latitude and longtitude coordinates

    >>> weather2 = Weather(apikey='341cddee0d757d3bfdff39f67b120f3c', lat=41.1, lon=-4.1)

    # Get a complete weather data for the next 12 hours:

    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:

    >>> weather1.next_12h_simplified()

    """

    def __init__(self, apikey=None, city=None, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon

        if self.city:
            req = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.apikey}'
                               f'&units=metric')
            self.data = req.json()
        elif self.lat and self.lon:
            req = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid='
                               f'{self.apikey}&units=metric')
            self.data = req.json()
        else:
            raise TypeError('Provide either a city or lat and lon args!')

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
        :return:
        Returns 3-hour data for the next 12 hours as a dict.
        """

        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        :return:
        Returns date, temperature, and sky condition every 3 hours for the next 12 hours as a tuple of tuples.
        """

        simple_data = []
        for weather_item in self.data['list'][:4]:
            simple_data.append((weather_item['dt_txt'], weather_item['main']['temp'],
                                weather_item['weather'][0]['description']))

        return simple_data


