class RTRating(object):
    def __init__(self, ratings):
        self.__critics_score = ratings[0]
        self.__audience_score = ratings[2]
        self.__link = None

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

    @property
    def link(self):
        return self.__link

    @link.setter
    def link (self, link):
        self.__link = link

    def __str__(self):
        return "{Critics score: " + self.critics_score + ", Audience score: " + self.audience_score + '}'
