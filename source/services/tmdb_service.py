import os
import requests


class TmdbService:

    __TMDB_API = 'https://api.themoviedb.org/3/movie/'
    __IMAGE_URL = 'https://image.tmdb.org/t/p/w342'

    def __init__(self, movie_id):
        self.id = movie_id

    def get_artwork(self):
        api_key = os.environ.get('TMDB_API_KEY')
        payload = {'api_key': api_key}
        response = requests.get(self.__TMDB_API + self.id + '?', data=payload)

        movie_info = response.json()
        artwork_url = movie_info['poster_path']

        return self.__IMAGE_URL + artwork_url
