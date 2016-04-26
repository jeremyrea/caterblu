import requests
import re

from bs4 import BeautifulSoup
from source.models.technical_specs import TechnicalSpecs


class ImdbService:

    __API_URL = 'http://www.imdb.com/xml/find?'
    __URL = 'http://www.imdb.com/title/'
    __SEPERATOR = '-'

    def __init__(self, title):
        self.title = title
        self.id = self.get_movie_id()

    def get_tech_spec(self):
        search_url = self.__URL + str(self.id) + '/technical?'
        payload = {'ref_': 'tt_dt_spec'}

        technical_page = requests.get(search_url, data=payload)
        contents = technical_page.text

        soup = BeautifulSoup(contents, 'lxml')
        data_table = soup.find('tbody')
        rows = data_table.find_all('td')

        specs = self.get_specs(rows)
        specs.link = technical_page.url

        return specs

    def get_artwork(self):
        search_url = self.__URL + str(self.id)
        movie_page = requests.get(search_url)

        contents = movie_page.text
        soup = BeautifulSoup(contents, 'lxml')

        return self.get_artwork_url(soup)


    def get_movie_id(self):
        search_title = self.format_title()
        payload = {'json': '1', 'nr': 1, 'tt': 'on', 'q': search_title}

        response = requests.post(self.__API_URL, data=payload)

        movie_info = response.json()

        try:
            movie_id = movie_info['title_popular'][0]['id']
        except:
            movie_id = movie_info['title_approx'][0]['id']

        return movie_id

    def format_title(self):
        return self.title.replace(' ', self.__SEPERATOR)

    def get_specs(self, rows):
        tech_specs = TechnicalSpecs()

        for i in range(len(rows)):
            if 'Negative Format' in rows[i].get_text():
                tech_specs.negative_format = self.format_specification(rows[i])
            elif 'Cinematographic Process' in rows[i].get_text():
                tech_specs.cinematographic_process = self.format_specification(rows[i])

        return tech_specs

    def format_specification(self, cell):
        specs = list(cell.find_next_sibling('td').stripped_strings)

        output = []
        ''' Strip newline characters left from stripped_strings'''
        for spec in specs:
            output.append(re.sub('\s+', ' ', spec))

        return output

    def get_artwork_url(self, soup):
        poster_div = soup.find('div', {'class': 'poster'})
        image_tag = poster_div.find('img')
        url = image_tag.get('src')

        return self.format_artwork_url(url)

    def format_artwork_url(self, url):
        formatted_url = url
        formatted_url = formatted_url.replace('UY268_', 'UY500_')
        formatted_url = formatted_url.replace('_CR4,', '_CR0,')
        formatted_url = formatted_url.replace('_CR6,', '_CR0,')
        formatted_url = formatted_url.replace(',182,', ',500,')
        formatted_url = formatted_url.replace(',268_', ',500_')
        formatted_url = formatted_url.replace('_CR0,', '_UY0,')

        return formatted_url
