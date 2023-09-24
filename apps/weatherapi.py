import requests 
from apps.constants import TOKENWEATHERAPI


class Requests: 
    def __init__(self, token) -> None: 
        self.token = token 
 
    def getWeather(self, city: str) -> requests.Response: 
        params = { 
            'key': self.token,
            'q': city,
            'lang': 'ru',
            'alerts': 'yes'
        } 
        return requests.get(f'http://api.weatherapi.com/v1/current.json', params=params) 
