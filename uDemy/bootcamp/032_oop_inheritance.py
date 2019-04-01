class Animal:
    cool = True

    def make_sound(self, sound):
        print("This animal says {}".format(sound))

class Cat(Animal):
    pass

""" 
puss = Cat()

puss.make_sound("Shrrriiiiiiiek")
print(Animal.cool)
print(Cat.cool)
print(puss.cool)
 """

class Human:
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
    


jan = Human("Jan", "Bier", 9)
print(jan)
jan.age = 37
print(jan)