from multiprocessing.pool import ThreadPool
from source.services.amazon_service import AmazonService
from source.services.bluray_service import BlurayService
from source.services.imdb_service import ImdbService
from source.services.itunes_service import ItunesService
from source.services.rotten_tomatoes_service import RottenTomatoesService


class CaterController:

    __THREAD_COUNT = 5

    def __init__(self, title):
        self.title = title

    def get_data(self):
        amazon_service = AmazonService(self.title)
        bluray_service = BlurayService(self.title)
        imdb_service = ImdbService(self.title)
        itunes_service = ItunesService(self.title)
        rotten_tomatoes_service = RottenTomatoesService(self.title)

        pool = ThreadPool(processes=self.__THREAD_COUNT)

        async_rt_rating = pool.apply_async(rotten_tomatoes_service.get_rt_rating)
        async_bluray_rating = pool.apply_async(bluray_service.get_bluray_rating)
        async_tech_specs = pool.apply_async(imdb_service.get_tech_spec)
        async_price = pool.apply_async(amazon_service.get_price)
        async_artwork = pool.apply_async(itunes_service.get_artwork)
        pool.close()

        try:
            rt_rating = async_rt_rating.get()
            bluray_rating = async_bluray_rating.get()
            tech_specs = async_tech_specs.get()
            price = async_price.get()
            artwork = async_artwork.get()
            pool.join()
        except:
            raise ValueError("Oops, something went wrong")

        data = {'rt_rating': rt_rating,
                'bluray_rating': bluray_rating,
                'tech_specs': tech_specs,
                'price': price,
                'artwork': artwork}

        return data
