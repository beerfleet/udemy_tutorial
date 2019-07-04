class Animal:
    cool = True

    def __init__(self, name, species):
        self._name = name
        self._species = species

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

    def __repr__(self):
        return "{} is a {}".format(self._name, self._species)

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, "Cat")
        self._breed = breed
        self._toy = toy

    def make_sound(self):
        print("This animal says Meeeeoowwww")

class Human(Animal):
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        self._age = age

    def __repr__(self):
        return "{} {} is {} years old.".format(self._first, self._last, self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative")
    
cat = Cat("Jake", "Drunken cat", "birdie!")
cat2 = Cat("Kit", "Kateter", "mossel")
cat2.make_sound()
print(cat2._species)