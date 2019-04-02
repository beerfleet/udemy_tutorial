class Character:
    def __init__(self, name, hp, level):
        self.name = name
        if not isinstance(hp, int):
            raise ValueError("Hit points has to be an integer value.")
        self.hp = hp
        if not isinstance(level, int):
            raise ValueError("Level has to be an integer value.")
        self.level = level

class NPC(Character):
    def speak(self):
        print("I heard there were monsters running around last night!")

""" 
villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
villager.speak()
"""

class Aquatic:
    def __init__(self, name):
        print("**** AQUATIC INIT *****")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("**** AMBULATORY INIT *****")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):        
        super().__init__(name = name)
        Aquatic.__init__(self, name = name)
        print("***** PENGUIN INIT ********")

pengo = Penguin("Pengo")
print(pengo.greet())