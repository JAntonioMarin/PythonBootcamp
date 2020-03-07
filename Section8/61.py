class Dog():
    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and my number is {}".format(self.name, number))


my_dog = Dog(breed='Lab', name='Sam', spots=False)

print(my_dog.species)

my_dog.bark(1)


class Circle():
    # Class Object attribute
    pi = 3.14

    def __init__(self, radius=10):
        self.radius = radius
        self.area = radius*radius*self.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()

print(my_circle.pi)

print(my_circle.get_circumference())

print(my_circle.area)
