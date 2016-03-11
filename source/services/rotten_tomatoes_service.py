import requests
import re

from bs4 import BeautifulSoup
from source.models.rt_rating import RTRating


class RottenTomatoesService:

    __URL = 'http://www.rottentomatoes.com/m/'

    def __init__(self, title):
        self.title = title

    def get_rt_rating(self):
        search_url = self.__URL + self.format_title()

        movie_page = requests.get(search_url)
        contents = movie_page.text
        soup = BeautifulSoup(contents, 'lxml')

        return self.get_ratings(soup)

    def format_title(self):
        return self.title.replace(' ', '_')

    def get_ratings(self, soup):
        items = []

        for item in soup.findAll(attrs={'itemprop': 'ratingValue'}):
            items.append(item.get_text().strip('%'))

        return RTRating(items)
