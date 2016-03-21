import requests
import re

from bs4 import BeautifulSoup
from source.models.bluray_rating import BlurayRating


class BlurayService:

    __URL = 'http://www.blu-ray.com/search/?'

    def __init__(self, title):
        self.title = title

    def get_bluray_rating(self):
        search_title = self.format_title()
        payload = 'quicksearch=1&section=bluraymovies&quicksearch_keyword=' + search_title
        search_url = self.__URL + payload

        movie_page = requests.get(search_url)
        contents = movie_page.text
        soup = BeautifulSoup(contents, 'lxml')

        movie_url = self.get_movie_url(soup)
        movie_page = requests.get(movie_url)
        contents = movie_page.text
        soup = BeautifulSoup(contents, 'lxml')

        review_rows = self.get_bluray_review_cells(soup)

        ratings = self.get_ratings(review_rows)
        ratings.link = movie_url

        return ratings

    def format_title(self):
        return self.title.replace(' ', '+')

    def get_movie_url(self, soup):
        movie_element = soup.find('a', {'title': re.compile(self.title + '.*')})
        movie_url = ''
        if(movie_element):
            movie_url = movie_element['href']

        return movie_url

        ### This would allow to get retrieve multiple release versions
        # movies = []
        # for a in soup.find_all('a', title=True):
        #     if(self.title in a['title']):
        #         movies.append(a['href'])
        #
        # return movies[0]

    def get_bluray_review_cells(self, soup):
        review_section = soup.find('div', {'id': 'bluray_rating'})
        review_table = review_section.find('table')
        rows = review_table.find_all('td')

        return rows

    def get_ratings(self, review_rows):
        bluray_rating = BlurayRating()

        for i in range(len(review_rows)):
            if 'Video' in review_rows[i].get_text():
                bluray_rating.video = review_rows[i + 2].get_text()
            elif 'Audio' in review_rows[i].get_text():
                bluray_rating.audio = review_rows[i + 2].get_text()
            elif 'Extras' in review_rows[i].get_text():
                bluray_rating.extras = review_rows[i + 2].get_text()

        return bluray_rating
