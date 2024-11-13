class Flight:
    """take the data of a flight, such as the flight number, flight origin, flight destination, number of passengers
    total flight weight, the name of the pilot and the name of the crew members, and display the flight data to the user

    Attributes:
        number: is the flight number
        origin: is the city from which the flight has taken of
        destination: is the city to which the flight will arrive
        num_passengers: is the total number of the passengers of the flight
        total weight: is the total weight of the flight
        pilot: is the name of the pilot who is in charge of the plane control
        crew: is the name of the crew of the flight

    Methode:
        display_flight_data(self):
            return the arguments of the class
    """
    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """
        Arguments:
             number (integer): it is the flight number, and it is either an integer or a string
             origin (string): it is the name of the city from which the airplane is taking off
             destination (string): it is the name of the city from which the airplane is going to land
             num_passengers(integer): it is the number of the passengers that the airplane will carry
             total_weight (float): it is the total weight of the airplane in kilograms
             pilot (string) : it is the name of the pilot of the plane
             crew (list of strings): it is a list containing all crew members' name in the plane
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

    @property
    def total_weight(self):
        """ Return the total weight of the plane in kilograms
        it is a float and, sums the weights of that is inclusive to the plane
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """ return the name of the pilot
        it is a string and, it is the name of the person who is piloting the plane from the origin to the destination
        """
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """ return the names of the crew

        it is a list of strings containing the names of the crew of the flight
        """
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew

    def display_flight_data(self):
        """ Print the attributes of the class Flight

        it prints the flight number, the number of passengers, the total weight, the pilot name and the list of crew members
        """
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self._total_weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)