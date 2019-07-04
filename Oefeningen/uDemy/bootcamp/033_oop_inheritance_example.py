class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):        
        return "There are currently {}".format(cls.active_users)

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return "{} has logged out".format(self.first)

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def initials(self):
        return "{}.{}".format(self.first[0], self.last[0])
    
    def likes(self, thing):
        return "{} likes {}".format(self.first, thing)

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return "Happy {}th, {}".format(self.age, self.first)

class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return "{} removed a post from {} community".format(self.full_name, self.community)

print(User.display_active_users())
u1 = User("Tom", "Jones", 45)
print(User.display_active_users())
jasmine = Moderator("Sarah", "O'Connor", 41, "Survivor")
print(User.display_active_users())