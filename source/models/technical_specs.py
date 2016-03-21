class TechnicalSpecs(object):
    def __init__(self):
        self.__negative_format = None
        self.__cinematographic_process = None
        self.__link = None

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

    @property
    def link(self):
        return self.__link

    @link.setter
    def link (self, link):
        self.__link = link

    def __str__(self):
        return "{Negative format: " + str(self.negative_format) + ", Cinematographic process: " + str(
            self.cinematographic_process) + "}"
