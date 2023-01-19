from domain.Flight import Flight


class Service:

    def __init__(self, repository):
        self.__repository = repository

    def add(self, identifier, departure_city, departure_time, arrival_city, arrival_time):
        data = list(self.__repository.get_data())

        flight = Flight(identifier, departure_city, departure_time, arrival_city, arrival_time)

        data.append(flight)

        self.__repository.save(data)

    def remove(self, identifier):
        data = list(self.__repository.get_data())

        for flight in data:
            if flight.get_identifier() == identifier:
                data.remove(flight)

        self.__repository.save(data)

    def get_data(self):
        return self.__repository.get_data()
