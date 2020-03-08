class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('Im eating')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):  # Override
        print('I am a dog')

    def bark(self):
        print('WOOF!')


my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()


# Polymorphism

class Dog2():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + "says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says miau!"


niko = Dog2("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet_class in [niko, felix]:
    print(type(pet_class))
    print(type(pet_class.speak()))


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal3():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


my_animal = Animal3('Fred')


# my_animal.speak()

class Dog3(Animal3):
    def speak(self):
        return self.name + " says woof!"


class Cat3(Animal3):
    def speak(self):
        return self.name + " says miau!"


fido = Dog3("Fido")
isis = Cat3("Isis")

print(fido.speak())
print(isis.speak())
