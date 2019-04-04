class Animal():
    def say(self):
        raise NotImplementedError("Define speech in concrete classes")
    
    def __repr__(self):
        return f"Not a concrete animal !!!!"

class Cat(Animal):
    def say(self):
        return "Miaaaaw"
    
    def __repr__(self):
        return f"Cat"

class Dog(Animal):
    def say(self):
        return "Waaaarf"
    
    def __repr__(self):
        return "Dog"

class Zoo():
    
    def talks_to(self, animal1, animal2):
        if not isinstance(animal1, Animal):
            raise ValueError(f"{animal1} is not a valid animal")
        if not isinstance(animal2, Animal):
            raise ValueError(f"{animal2} is not a valid animal")
        print(f"{animal1} says {animal1.say()}, {animal2} responds {animal2.say()} !!!")


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    zoo = Zoo()
    zoo.talks_to(dog, int)
