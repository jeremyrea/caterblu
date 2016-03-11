import requests
import itunespy


class ItunesService:

    __URL = 'https://itunes.apple.com/lookup?'

    def __init__(self, title):
        self.id = self.get_movie_id(title)

    def get_artwork(self):
        artwork_key = 'artworkUrl100'

        '''Can also set country by adding
                &country=$COUNTRY
           in payload
        '''
        payload = {'id': str(self.id)}

        response = requests.post(self.__URL, data=payload)
        data = response.json()
        image_address = data['results'][0][artwork_key]

        # Does not work in Chrome
        #image_address = image_address.replace('http', 'https')
        image_address = self.set_larger_image(image_address)

        return image_address

    def get_movie_id(self, title):
        movies = itunespy.search_movie(title)
        movie_id = movies[0].track_id

        return movie_id

    def set_larger_image(self, image_address):
        return image_address.replace('100x100', '500x500')
