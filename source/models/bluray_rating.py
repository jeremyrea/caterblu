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
