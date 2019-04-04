class Animal():
    def say(self):
        raise NotImplementedError("Define speech in concrete classes")

class Cat(Animal):
    def say(self):
        return "Miaaaaw"

class Dog(Animal):
    def say(self):
        return "Waaaarf"

class Zoo():
    
    def talks_to(self, animal1, animal2):
        print(f"Animal 1 says {animal1.say()}, Animal 2 responds {animal2.say()} !!!")

cat = Cat()
dog = Dog()
zoo = Zoo()

zoo.talks_to(dog, cat)