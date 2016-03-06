import requests
import re
import os
import itunespy
import json

from amazon.api import AmazonAPI
from bs4 import BeautifulSoup
from .models import TechnicalSpecs
from .models import BlurayRating
from .models import RTRating
from .models import Price

def get_rt_rating(title):
    domain = "http://www.rottentomatoes.com/"
    query = "m/" + title.replace(' ', '_')
    url = domain + query

    r = requests.get(url)
    contents = r.text

    soup = BeautifulSoup(contents)
    items = []
    for item in soup.findAll(attrs={'itemprop': 'ratingValue'}):
        items.append(item.get_text().strip('%'))

    ratings = RTRating(items)

    return ratings


def get_tech_spec(title):
    url = 'http://www.imdb.com/xml/find?'
    payload = {'json': '1', 'nr': 1, 'tt': 'on', 'q': title.replace(' ', '-')}

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
            tech_specs.negative_format = build_specification(cells[i])
        elif 'Cinematographic Process' in cells[i].get_text():
            tech_specs.cinematographic_process = build_specification(cells[i])

    return tech_specs


def build_specification(cell):
    specs = list(cell.find_next_sibling('td').stripped_strings)

    output = []
    ''' Strip newline characters left from stripped_strings'''
    for spec in specs:
        output.append(re.sub('\s+', ' ', spec))

    return output


def get_bluray_rating(title):
    domain = 'http://www.blu-ray.com/'
    search = 'search/?'
    payload = 'quicksearch=1&quicksearch_keyword=' + title.replace(' ', '+')
    search_url = domain + search + payload

    r = requests.get(search_url)
    contents = r.text

    soup = BeautifulSoup(contents)
    movie_url = soup.find('a', {'title': re.compile(title + '.*')})['href']

    ratings_page = requests.get(movie_url)
    contents = ratings_page.text
    soup = BeautifulSoup(contents)

    review_section = soup.find('div', {'id': 'bluray_rating'})
    review_table = review_section.find('table')
    cells = review_table.find_all('td')

    bluray_rating = BlurayRating()

    for i in range(len(cells)):
        if 'Video' in cells[i].get_text():
            bluray_rating.video = cells[i + 2].get_text()
        elif 'Audio' in cells[i].get_text():
            bluray_rating.audio = cells[i + 2].get_text()
        elif 'Extras' in cells[i].get_text():
            bluray_rating.extras = cells[i + 2].get_text()

    return bluray_rating


def get_price(title):
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    associates_tag = os.environ.get('AWS_ASSOCIATES_TAG')

    amazon = AmazonAPI(access_key, secret_key, associates_tag, Region='CA', Version='2013-08-01')

    product = amazon.search_n(1, Keywords=title, SearchIndex='All')[0]

    price = Price()
    price.price = product.price_and_currency
    price.list_price = product.list_price

    return price

def get_artwork(title):
    movies = itunespy.search_movie(title)
    movie_id = movies[0].track_id
    
    url = 'https://itunes.apple.com/lookup?id=' + str(movie_id)
    response = requests.get(url)
    data = response.json()
    image_address = data['results'][0]['artworkUrl100']
    image_address = image_address.replace('100x100', '500x500')
    
    return image_address    