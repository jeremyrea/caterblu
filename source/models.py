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
        return "{Negative format: " + str(self.negative_format) + ", Cinematographic process: " + str(self.cinematographic_process) + "}"


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
