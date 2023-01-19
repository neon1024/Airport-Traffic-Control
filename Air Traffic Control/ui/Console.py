class Console:

    def __init__(self, service, repository):
        self.__service = service
        self.__repository = repository

        self.__console_options = {
            "1": self.__add_flight,
            "2": self.__delete_flight,
            "3": self.__display_airports_in_decreasing_order_of_activity,
            "4": self.__display_time_intervals_with_no_flights_in_decreasing_order_of_length,
            "5": self.__display_maximum_number_of_flights_under_the_backup_radar,
            "x": exit
        }

    def __add_flight(self):
        identifier = input("Identifier: ")
        departure_city = input("Departure City: ")
        departure_time = input("Departure Time: ")
        arrival_city = input("Arrival City: ")
        arrival_time = input("Arrival Time: ")

        data = list(self.__service.get_data())

        # check if id is unique
        for flight in data:
            if flight.get_identifier() == identifier:
                print("[!] Identifier not unique")
                return

        # flight times are between 15 and 90 min
        if ":" not in departure_time or ":" not in arrival_time:
            print("[!] Invalid time format")
            return

        first_time_token = departure_time.split(":")
        first_hour = int(first_time_token[0])
        first_min = int(first_time_token[1])

        second_time_token = arrival_time.split(":")
        second_hour = int(second_time_token[0])
        second_min = int(second_time_token[1])

        if first_hour > second_hour:
            print("[!] Invalid time")
            return

        if first_hour == second_hour:
            if second_min - first_min < 15 or second_min - first_min > 90:
                print("[!] Invalid time")
                return

        hour_dif = second_hour - first_hour
        minutes = hour_dif*60
        min_dif = second_min - first_min
        minutes -= min_dif

        if minutes < 15 or minutes > 90:
            print("[!] Invalid time")
            return

        # departure_time must be unique for any time of the departure_city
        # same for arrival_time
        for flight in data:
            obj_departure_city = flight.get_departure_city()
            obj_arrival_city = flight.get_arrival_city()
            if obj_arrival_city == arrival_city or obj_arrival_city == departure_city or obj_departure_city == arrival_time or obj_departure_city == departure_time:
                obj_departure_time = flight.get_departure_time()
                obj_arrival_time = flight.get_arrival_time()
                if obj_arrival_time == departure_time or obj_arrival_time == arrival_time or obj_departure_time == departure_time or obj_departure_time == arrival_time:
                    print("[!] An airport can handle a single departure or arrival during each minute")
                    return

        self.__service.add(identifier, departure_city, departure_time, arrival_city, arrival_time)

        print("[+] Flight added")

    def __delete_flight(self):
        identifier = input("Identifier: ")

        data = list(self.__service.get_data())

        for flight in data:
            if flight.get_identifier() == identifier:
                self.__service.remove(identifier)
                print("[-] Flight removed")
                return

        print("[!] Identifier not found")

    def __display_airports_in_decreasing_order_of_activity(self):
        pass

    def __display_time_intervals_with_no_flights_in_decreasing_order_of_length(self):
        pass

    def __display_maximum_number_of_flights_under_the_backup_radar(self):
        pass

    @staticmethod
    def __print_console_options():
        print("1: Add a new flight")
        print("2: Delete a flight")
        print("3: List the airports, in decreasing order of activity")
        print("4: List the time intervals during which no flights are taking place, in decreasing order of length")
        print("5: The tracking radar suffers a failure. The backup radar can be used, but it can only track a single flight at a time. Determine the maximum number of flights that can proceed as planned")
        print("x: Exit")

    def run_console(self):

        while True:
            try:

                self.__print_console_options()

                chosen_option = input("> ")

                self.__console_options[chosen_option]()

            except Exception as error:
                print(str(error))
