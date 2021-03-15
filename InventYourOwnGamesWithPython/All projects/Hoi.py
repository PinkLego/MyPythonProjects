class Mammal:
    def walk(self):
        print("walking")
    def drink(self):
        print("drinking")
    def eliminating_waste(self):
        print("peeing")

class Dog(Mammal):
    pass

class Human(Mammal):
    pass

class Cat(Mammal):
    pass

Human1 = Human()
Human1.drink()

Dog1 = Dog()
Dog1.walk()

Cat1 = Cat()
Cat1.eliminating_waste()