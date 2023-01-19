class Flight:

    def __init__(self, identifier, departure_city, departure_time, arrival_city, arrival_time):
        self.__identifier = identifier
        self.__departure_city = departure_city
        self.__departure_time = departure_time
        self.__arrival_city = arrival_city
        self.__arrival_time = arrival_time

    def get_identifier(self):
        return self.__identifier

    def set_identifier(self, new_identifier):
        self.__identifier = new_identifier

    def get_departure_city(self):
        return self.__departure_city

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_city(self):
        return self.__arrival_city

    def get_arrival_time(self):
        return self.__arrival_time

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.__identifier},{self.__departure_city},{self.__departure_time},{self.__arrival_city},{self.__arrival_time}"
