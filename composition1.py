"""
Build a flight crew consisting of:
pilot
copilot
flight_attendant
"""


class FlightCrew:
    def __init__(self, pilot, copilot, flight_attendant):
        self.pilot = pilot
        self.copilot = copilot
        self.flight_attendant = flight_attendant

    def __str__(self):
        return (f'{self.pilot}\n'
                f'{self.copilot}\n'
                f'{self.flight_attendant}')


class CrewMember:
    def __init__(self, name):
        self.name = name


class Pilot(CrewMember):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The crew's pilot is {self.name}"


class Copilot(CrewMember):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The crew's copilot is {self.name}"


class FlightAttendant(CrewMember):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The crew's flight attendant is {self.name}"


def main():
    pilot = Pilot('Bob')
    copilot = Copilot('Sue')
    flight_attendant = FlightAttendant('Larry')

    flight_crew = FlightCrew(pilot, copilot, flight_attendant)

    print(flight_crew)


if __name__ == '__main__':
    main()
