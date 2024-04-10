class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        raise NotImplementedError("Subclasses must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

if __name__ == "__main__":
    dog = Dog("Buddy", "Dog")
    cat = Cat("Whiskers", "Cat")

    print(f"{dog.name} the {dog.species} says: {dog.sound()}")
    print(f"{cat.name} the {cat.species} says: {cat.sound()}")
