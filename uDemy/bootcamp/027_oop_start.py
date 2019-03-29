class User:
    
    active_users = 0

    def __init__(self, name, age, weight):
        self.name = name[0].upper() + name[1:].lower()
        self.age = age
        print(f"{self.name}'s Age is now {self.age}")
        self.weight = weight
        self.__msg = "Massage!"
        User.active_users += 1

    def __repr__(self):
        return f"User object: {self.name}, {self.age}, {self.weight}"
        
    def weight_in_pounds(self):
        return self.weight * 2.2046

    def birthday(self):
        self.age += 1
        return f"Yikes, it's a birthday. {self.name}'s age is now {self.age}"

    @classmethod
    def display_active_users(clss):
        print(clss)

    @classmethod
    def from_string(clss, datastring):
        par_list = datastring.split(",")
        return clss(par_list[0], int(par_list[1]), float(par_list[2]))

# ***********************************************************
# ***********************************************************

user1 = User('jAkKE', 37, 74.25)
user2 = User('PjöTTr', 38, 65.32)
user3 = User('klEENeX', 39, 80.20)
user3 = User('CondOrIto', 39, 80.20)

# print(f"{user2.name}, age {user2.age}, weight {user2.weight}")

# print(dir(user1))
print(user1._User__msg)
print(user1.weight_in_pounds())
print(user3.birthday())
print (f"Aantal gebruikers = {User.active_users}")
print(User.display_active_users())
str_user = User.from_string("Jezz,88,79.45")
print(str_user)
print(type(str_user.weight))

print(user1)