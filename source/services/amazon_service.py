import os
import re

from amazon.api import AmazonAPI
from source.models.price import Price


class AmazonService:

    __API_VERSION = '2013-08-01'

    def __init__(self, title, country):
        self.title = title
        self.country = country

        env_vars = self.get_amazon_env_variables()
        self.amazon = AmazonAPI(env_vars['access_key'],
                                env_vars['secret_key'],
                                env_vars['associates_tag'],
                                Region=self.country,
                                Version=self.__API_VERSION)

    def get_price(self):
        products = self.amazon.search_n(10,
                                        Keywords=self.title + ' [Blu-ray]',
                                        SearchIndex='All')

        ranked_products = self.rank_products(products)
        product = ranked_products[0]

        price = Price()
        price.price = list(product.price_and_currency)
        price.list_price = list(product.list_price)
        price.link = product.offer_url

        return price

    def rank_products(self, products):
        ranked_products = sorted(products, key=lambda x: self.product_score(x), reverse=True)

        return ranked_products

    def product_score(self, p):
        title = str(p.title)
        title = title.replace('[Blu-ray]', '')
        title = title.replace('(Bilingual)', '')
        title = title.replace('(Region Free)', '')
        title = title.strip(' ')
        size_diff = abs(len(title) - len(self.title))

        p_score = 1 if size_diff == 0 else 0
        p_score += 1 if re.search('[Blu\-ray]', p.title) else p_score

        return p_score

    def get_amazon_env_variables(self):
        access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        associates_tag = os.environ.get('AWS_ASSOCIATES_TAG')

        env_variables = {'access_key': access_key,
                         'secret_key': secret_key,
                         'associates_tag': associates_tag}

        return env_variables
