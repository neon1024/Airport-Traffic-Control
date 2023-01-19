from domain.Flight import Flight


class Repo:

    def __init__(self):
        self.__data = []
        self.__load()

    def __load(self):
        IDENTIFIER = 0
        DEPARTURE_CITY = 1
        DEPARTURE_TIME = 2
        ARRIVAL_CITY = 3
        ARRIVAL_TIME = 4

        data = []

        with open("C:/Users/rober/Desktop/Air Traffic Control/repository/flight_information.txt", "r") as file:
            for line in file:
                token = line.strip()
                token = token.split(",")

                identifier = token[IDENTIFIER]
                departure_city = token[DEPARTURE_CITY]
                departure_time = token[DEPARTURE_TIME]
                arrival_city = token[ARRIVAL_CITY]
                arrival_time = token[ARRIVAL_TIME]

                flight = Flight(identifier, departure_city, departure_time, arrival_city, arrival_time)
                data.append(flight)

        self.__data = data

    def save(self, new_data):
        self.__data = new_data

        with open("C:/Users/rober/Desktop/Air Traffic Control/repository/flight_information.txt", "w") as file:

            for data in self.__data:
                file.write(str(data) + "\n")

    def get_data(self):
        return self.__data
