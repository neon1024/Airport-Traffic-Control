import unittest

from domain.Flight import Flight
from repository.Repo import Repo
from service.Service import Service


class TestService(unittest.TestCase):

    def setUp(self) -> None:
        self.__repository = Repo()
        self.__service = Service(self.__repository)

    def tearDown(self) -> None:
        del self.__repository
        del self.__service

    def test_add_flight(self):
        data = list(self.__repository.get_data())
        initial_length = len(data)

        identifier = 100
        departure_city = "Cluj"
        departure_time = "10:00"
        arrival_city = "Bucharest"
        arrival_time = "11:00"

        self.__service.add(identifier, departure_city, departure_time, arrival_city, arrival_time)

        data = list(self.__repository.get_data())
        updated_length = len(data)

        self.assertEqual(initial_length, updated_length - 1)

    def test_delete_flight(self):
        data = list(self.__repository.get_data())
        initial_length = len(data)

        identifier = 100
        departure_city = "Cluj"
        departure_time = "10:00"
        arrival_city = "Bucharest"
        arrival_time = "11:00"

        self.__service.add(identifier, departure_city, departure_time, arrival_city, arrival_time)

        flight = Flight(identifier, departure_city, departure_time, arrival_city, arrival_time)

        self.__service.remove(100)

        data = list(self.__repository.get_data())
        updated_length = len(data)

        self.assertEqual(initial_length, updated_length)
