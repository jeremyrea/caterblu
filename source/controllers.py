from bs4 import BeautifulSoup

import requests
import re
from .models import TechnicalSpecs
from .models import BlurayRating


def get_rt_rating():
    url = "http://www.rottentomatoes.com/m/the_martian/"

    r = requests.get(url)
    contents = r.text

    soup = BeautifulSoup(contents)
    items = []
    for item in soup.findAll(attrs={'itemprop': 'ratingValue'}):
        items.append(item.get_text() + '\n')

    # Returns All critics / Top critics / Audience score
    return items


def get_tech_spec():
    url = 'http://www.imdb.com/xml/find?'
    payload = {'json': '1', 'nr': 1, 'tt': 'on', 'q': 'the-martian'}

    response = requests.post(url, data=payload)

    movie_info = response.json()
    movie_id = movie_info['title_popular'][0]['id']

    domain = 'http://www.imdb.com/'
    search = 'title/' + movie_id + '/'
    payload = 'technical?ref_=tt_dt_spec'
    url = domain + search + payload

    r = requests.get(url)
    contents = r.text

    soup = BeautifulSoup(contents)
    table = soup.find('tbody')

    tech_specs = TechnicalSpecs()
    cells = table.find_all('td')

    for i in range(len(cells)):
        if 'Negative Format' in cells[i].get_text():
            tech_specs.negative_format = list(cells[i].find_next_sibling('td').stripped_strings)
        elif 'Cinematographic Process' in cells[i].get_text():
            tech_specs.cinematographic_process = list(cells[i].find_next_sibling('td').stripped_strings)

    return tech_specs


def get_bluray_rating():
    domain = 'http://www.blu-ray.com/'
    search = 'search/?'
    payload = 'quicksearch=1&quicksearch_keyword=The+Martian'
    search_url = domain + search + payload

    r = requests.get(search_url)
    contents = r.text

    soup = BeautifulSoup(contents)
    movie_url = soup.find('a', {'title': re.compile('The Martian.*')})['href']

    ratings_page = requests.get(movie_url)
    contents = ratings_page.text
    soup = BeautifulSoup(contents)

    review_section = soup.find('div', {'id': 'bluray_rating'})
    review_table = review_section.find('table')
    cells = review_table.find_all('td')

    bluray_rating = BlurayRating()

    for i in range(len(cells)):
        if 'Video' in cells[i].get_text():
            bluray_rating.video = cells[i+2].get_text()
        elif 'Audio' in cells[i].get_text():
            bluray_rating.audio = cells[i+2].get_text()
        elif 'Extras' in cells[i].get_text():
            bluray_rating.extras = cells[i+2].get_text()

    return bluray_rating
