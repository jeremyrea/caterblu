import requests
import re

from bs4 import BeautifulSoup
from source.models.technical_specs import TechnicalSpecs


class ImdbService:

    __API_URL = 'http://www.imdb.com/xml/find?'
    __URL = 'http://www.imdb.com/title/'

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

        return self.get_specs(rows)

    def get_movie_id(self):
        search_title = self.format_title()
        payload = {'json': '1', 'nr': 1, 'tt': 'on', 'q': search_title}

        response = requests.post(self.__API_URL, data=payload)

        movie_info = response.json()
        movie_id = movie_info['title_popular'][0]['id']

        return movie_id

    def format_title(self):
        return self.title.replace(' ', '-')

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
