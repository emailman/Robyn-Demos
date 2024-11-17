"""
Create a balloon object with 3 properties
Use a __str__ function to print the properties
Hide the properties that can not be changed
"""


class Balloon:
    def __init__(self, color, size):
        self.__color = color
        self.__size = size
        self.inflated = False

    def __str__(self):
        is_inflated = 'is' if self.inflated else 'is not'
        return (f'{self.__color} balloon, '
                f'{self.__size} inch diameter,'
                f' {is_inflated} inflated')


def main():
    balloon1 = Balloon('red', 10)
    print(balloon1)
    balloon1.inflated = True
    print(balloon1)
    balloon1.__color__ = 'blue'  # this does not work
    print(balloon1)


if __name__ == '__main__':
    main()
