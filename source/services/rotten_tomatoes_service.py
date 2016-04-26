import requests

from bs4 import BeautifulSoup
from source.models.rt_rating import RTRating


class RottenTomatoesService:

    __URL = 'http://www.rottentomatoes.com/m/'
    __SEPERATOR = '_'
    __PAGE_NOT_FOUND = 404

    def __init__(self, title):
        self.title = title
        self.formatted_title = title

    def get_rt_rating(self):
        self.format_title()
        search_url = self.__URL + self.formatted_title
        movie_page = requests.get(search_url)

        if self.__PAGE_NOT_FOUND == movie_page.status_code:
            self.format_title_second_pass()
            search_url = self.__URL + self.formatted_title
            movie_page = requests.get(search_url)

        contents = movie_page.text
        soup = BeautifulSoup(contents, 'lxml')

        ratings = self.get_ratings(soup)
        ratings.link = search_url

        return ratings

    def format_title(self):
        if self.formatted_title.startswith('A '):
            self.formatted_title = self.formatted_title.replace('A ', '', 1)
        if "'s" in self.formatted_title:
            self.formatted_title = self.formatted_title.replace("'s", 's')

        self.formatted_title = self.formatted_title.replace(' ', self.__SEPERATOR)
        self.formatted_title = self.formatted_title.replace('-', '')
        self.formatted_title = self.formatted_title.replace(':', '')
        self.formatted_title = self.formatted_title.replace(',', '')
        self.formatted_title = self.formatted_title.replace('.', '')
        self.formatted_title = self.formatted_title.replace('&', 'and')


    def format_title_second_pass(self):
        if self.formatted_title.startswith('The_'):
            self.formatted_title = self.formatted_title.replace('The_', '', 1)


    def get_ratings(self, soup):
        items = []

        for item in soup.findAll(attrs={'itemprop': 'ratingValue'}):
            items.append(item.get_text().strip('%'))

        return RTRating(items)
