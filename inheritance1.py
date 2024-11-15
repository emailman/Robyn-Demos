"""
Create a Pet class with Dog and Cat subclasses
"""


class Pet:
    def __init__(self, name, age, age_unit, weight, weight_unit,
                 breed, sound=None, sex='Unknown'):
        self.name = name
        self.age = age
        self.age_unit = age_unit
        self.weight = weight
        self.weight_unit = weight_unit
        self.sound = sound
        self.sex = sex
        self.breed = breed

    def __str__(self):
        if isinstance(self, Cat):
            pet_type = 'cat'
        elif isinstance(self, Dog):
            pet_type = 'dog'
        else:
            pet_type = 'unknown'

        return (f'{self.name} is a {self.age} {self.age_unit} old '
                f'{self.breed} {self.sex} {pet_type} weighing '
                f'{self.weight} {self.weight_unit} '
                f'who says {self.sound}')


class Dog(Pet):
    def __init__(self, name, age, age_unit, weight, weight_unit,
                 breed, sex):
        sound = 'woof'
        super().__init__(name, age, age_unit, weight, weight_unit,
                         breed, sound, sex)


class Cat(Pet):
    def __init__(self, name, age, age_unit, weight, weight_unit,
                 breed, sex):
        sound = 'meow'
        super().__init__(name, age, age_unit, weight, weight_unit,
                         breed, sound, sex)


def main():
    pet1 = Cat('Fluffy', 6, 'month', 7,
               'lbs', 'Persian', 'female')

    pet2 = Dog('Rex', 3, 'year', 23,
               'lbs', 'Collie', 'male')

    print(pet1)
    print(pet2)


if __name__ == '__main__':
    main()
