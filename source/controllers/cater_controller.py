import source.services.view_models as view_models
from multiprocessing.pool import ThreadPool

class CaterController:

    THREAD_COUNT = 5

    def __init__(self, movie_title):
        self.movie_title = movie_title

    def get_data(self):
        pool = ThreadPool(processes=self.THREAD_COUNT)

        async_rt_rating = pool.apply_async(view_models.get_rt_rating, (self.movie_title,))
        async_bluray_rating = pool.apply_async(view_models.get_bluray_rating, (self.movie_title,))
        async_tech_specs = pool.apply_async(view_models.get_tech_spec, (self.movie_title,))
        async_price = pool.apply_async(view_models.get_price, (self.movie_title,))
        async_artwork = pool.apply_async(view_models.get_artwork, (self.movie_title,))
        pool.close()

        rt_rating = async_rt_rating.get()
        bluray_rating = async_bluray_rating.get()
        tech_specs = async_tech_specs.get()
        price = async_price.get()
        artwork = async_artwork.get()
        pool.join()

        return {'rt_rating': rt_rating, 'bluray_rating': bluray_rating, 'tech_specs': tech_specs, 'price': price, 'artwork': artwork}
