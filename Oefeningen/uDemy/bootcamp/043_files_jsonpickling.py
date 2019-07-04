import jsonpickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


def persist_cat_write():
    c = Cat("Ferri", "Shitcat", "Wool ball")
    persistent_cat = jsonpickle.encode(c)
    print(persistent_cat)
    with open("C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/cats.json", 'w') as cat_json:
        cat_json.write(persistent_cat)


def persist_cat_read():    
    with open("C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/cats.json", 'r') as cat_json:
        contents = cat_json.read()
        deserialized = jsonpickle.decode(contents)
        print(deserialized)

persist_cat_write()
persist_cat_read()