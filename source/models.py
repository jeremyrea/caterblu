class RTRating(object):
    def __init__(self, ratings):
        self.__critics_score = ratings[0]
        self.__audience_score = ratings[2]

    @property
    def critics_score(self):
        return self.__critics_score

    @critics_score.setter
    def critics_score(self, critics_score):
        self.__critics_score = critics_score

    @property
    def audience_score(self):
        return self.__audience_score

    @audience_score.setter
    def audience_score(self, audience_score):
        self.__audience_score = audience_score

    def __str__(self):
        return "{Critics score: " + self.critics_score + ", Audience score: " + self.audience_score + '}'


class TechnicalSpecs(object):
    def __init__(self):
        self.__negative_format = None
        self.__cinematographic_process = None

    @property
    def negative_format(self):
        return self.__negative_format

    @negative_format.setter
    def negative_format(self, negative_format):
        self.__negative_format = negative_format

    @property
    def cinematographic_process(self):
        return self.__cinematographic_process

    @cinematographic_process.setter
    def cinematographic_process(self, cinematographic_process):
        self.__cinematographic_process = cinematographic_process

    def __str__(self):
        return "{Negative format: " + str(self.negative_format) + ", Cinematographic process: " + str(
            self.cinematographic_process) + "}"


class BlurayRating(object):
    def __init__(self):
        self.__video = None
        self.__audio = None
        self.__extras = None

    @property
    def video(self):
        return self.__video

    @video.setter
    def video(self, video):
        self.__video = video

    @property
    def audio(self):
        return self.__audio

    @audio.setter
    def audio(self, audio):
        self.__audio = audio

    @property
    def extras(self):
        return self.__extras

    @extras.setter
    def extras(self, extras):
        self.__extras = extras

    def __str__(self):
        return "{Video: " + self.video + ", Audio: " + self.audio + ", Extras: " + self.extras + "}"


class Price(object):
    def __init__(self):
        self.__price = None
        self.__list_price = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def list_price(self):
        return self.__list_price

    @list_price.setter
    def list_price (self, list_price):
        self.__list_price = list_price

    def __str__(self):
        return "{Price: " + str(self.price) + ", List: " + str(self.list_price) + "}"