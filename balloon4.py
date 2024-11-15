"""
Create a balloon object with 3 properties
Use a __str__ function to print the properties
Hide the properties that can not be changed
Use a counter to count the number of balloons made
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
        return (f'{self.__color} balloon, '
                f'{self.__size} inch diameter,'
                f' {is_inflated} inflated\n'
                f'Number of balloons made: {Balloon.__counter}\n')


def main():
    balloon1 = Balloon('red', 10)
    print(balloon1)
    balloon1.inflated = True
    print(balloon1)
    balloon1.__color = 'blue'  # this does not work

    balloon2 = Balloon(color='blue', size=12)
    print(balloon2)


if __name__ == '__main__':
    main()
