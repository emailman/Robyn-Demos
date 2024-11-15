"""
Create a balloon object with 3 properties
Use a __str__ function to print the properties
"""


class Balloon:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.inflated = False

    def __str__(self):
        is_inflated = 'is' if self.inflated else 'is not'
        return (f'{self.color} balloon, {self.size} inch diameter,'
                f' {is_inflated} inflated')


def main():
    balloon1 = Balloon('red', 10)
    print(balloon1)
    balloon1.inflated = True
    print(balloon1)


if __name__ == '__main__':
    main()
