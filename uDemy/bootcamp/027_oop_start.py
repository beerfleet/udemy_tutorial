class User:
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__msg = "Massage!"


user1 = User('jakke', 37, 74.25)
user2 = User('pjöttr', 38, 65.32)
user3 = User('kleeneX', 37, 80.20)

# print(f"{user2.name}, age {user2.age}, weight {user2.weight}")

# print(dir(user1))
print(user1._User__msg)
