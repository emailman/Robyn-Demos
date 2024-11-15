"""
Create a balloon object with 3 properties
"""


class Balloon:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.inflated = False


def main():
    balloon1 = Balloon('red', 10)
    print(balloon1.color, balloon1.size, balloon1.inflated)
    balloon1.inflated = True
    print(balloon1.color, balloon1.size, balloon1.inflated)


if __name__ == '__main__':
    main()
