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
