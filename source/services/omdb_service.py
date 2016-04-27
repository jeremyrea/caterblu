import requests

from bs4 import BeautifulSoup
from source.models.rt_rating import RTRating


class OmdbService:

    __API_URL = 'http://www.omdbapi.com/?'

    def __init__(self, movie_id):
        self.id = movie_id

    def get_rt_rating(self):
        payload = {'i': self.id, 'plot': 'short', 'r': 'json', 'tomatoes': 'true'}
        response = requests.post(self.__API_URL, params=payload)
        movie_info = response.json()

        scores = []
        scores.append(movie_info['tomatoMeter'])
        scores.append(movie_info['tomatoUserMeter'])

        rt_rating = RTRating(scores)
        rt_rating.link = movie_info['tomatoURL']

        return rt_rating
