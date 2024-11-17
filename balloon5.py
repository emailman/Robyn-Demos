"""
Create a balloon object with 3 properties
Use a __str__ function to print the properties
Hide the properties that can not be changed
Use a counter to count the number of balloons made
Create several balloons in a list
"""


class Balloon:
    __counter = 0  # Hidden class variable

    def __init__(self, color, size):
        self.__color = color
        self.__size = size
        self.inflated = False
        Balloon.__counter += 1

    def __str__(self):
        is_inflated = 'is' if self.inflated else 'is not'
        return (f'{self.__color} balloon, {self.__size} inch diameter,'
                f' {is_inflated} inflated\n')


    @staticmethod
    def get_number_of_balloons():
        return f'Number of balloons made: {Balloon.__counter}\n'


def main():
    balloons = [Balloon('red', 10),
                Balloon('red', 10),
                Balloon('blue', 10),
                Balloon('blue', 12)]

    for balloon in balloons:
        print(balloon)
    print(Balloon.get_number_of_balloons())


if __name__ == '__main__':
    main()
