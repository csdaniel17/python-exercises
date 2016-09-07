# ex 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object
class Animal(object):
    pass

## class Dog is-a Animal
class Dog(object):
    def __init__(self, name):
        ## Dog has-a __init__ that takes parameters self and name
        self.name = name

## class Cat is-a Animal
class Cat(object):
    def __init__(self, name):
        ## Cat has-a __init__ that takes parameters self and name
        self.name = name

## class Person is-a object
class Person(object):
    def __init__(self, name):
        ## Person has-a __init__ that takes parameters self and name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## in order to run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## pet attribute of mary is-a Cat, satan
mary.pet = satan

## frank is-a Employee instance that makes salary 120000
frank = Employee("Frank", 120000)

## pet attribute of frank is-a Dog, rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is-a Halibut instance
harry = Halibut()
