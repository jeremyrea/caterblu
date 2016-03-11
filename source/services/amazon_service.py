import os

from amazon.api import AmazonAPI
from source.models.price import Price

class AmazonService:

    __API_VERSION = '2013-08-01'

    def __init__(self, title):
        self.title = title

        env_vars = self.get_amazon_env_variables()
        self.amazon = AmazonAPI(env_vars['access_key'],
                                env_vars['secret_key'],
                                env_vars['associates_tag'],
                                Region='CA',
                                Version=self.__API_VERSION)

    def get_price(self):
        products = self.amazon.search_n(1,
                                        Keywords=self.title,
                                        SearchIndex='All')
        product = products[0]

        price = Price()
        price.price = product.price_and_currency
        price.list_price = product.list_price

        return price

    def get_amazon_env_variables(self):
        access_key = os.environ.get('AWS_ACCESS_KEY_ID')
        secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        associates_tag = os.environ.get('AWS_ASSOCIATES_TAG')

        env_variables = {'access_key': access_key,
                         'secret_key': secret_key,
                         'associates_tag': associates_tag}

        return env_variables
