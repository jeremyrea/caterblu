from multiprocessing.pool import ThreadPool
from source.services.amazon_service import AmazonService
from source.services.bluray_service import BlurayService
from source.services.imdb_service import ImdbService
from source.services.tmdb_service import TmdbService
from source.services.omdb_service import OmdbService


class CaterController:

    __THREAD_COUNT = 5

    def __init__(self, title, country):
        self.title = title
        self.country = country

    def get_data(self):
        amazon_service = AmazonService(self.title, self.country)
        bluray_service = BlurayService(self.title)
        imdb_service = ImdbService(self.title)
        tmdb_service = TmdbService(imdb_service.get_id())
        omdb_service = OmdbService(imdb_service.get_id())

        pool = ThreadPool(processes=self.__THREAD_COUNT)
        async_rt_rating = pool.apply_async(omdb_service.get_rt_rating)
        async_bluray_rating = pool.apply_async(bluray_service.get_bluray_rating)
        async_tech_specs = pool.apply_async(imdb_service.get_tech_spec)
        async_artwork = pool.apply_async(tmdb_service.get_artwork)
        async_price = pool.apply_async(amazon_service.get_price)
        pool.close()

        # try:
        rt_rating = async_rt_rating.get()
        bluray_rating = async_bluray_rating.get()
        tech_specs = async_tech_specs.get()
        price = async_price.get()
        artwork = async_artwork.get()
        pool.join()
        # except:
        #     raise ValueError("Oops, something went wrong")

        data = {'rt_rating': rt_rating,
                'bluray_rating': bluray_rating,
                'tech_specs': tech_specs,
                'price': price,
                'artwork': artwork}

        return data

    def get_price(self):
        amazon_service = AmazonService(self.title, self.country)
        price = amazon_service.get_price()

        return price
