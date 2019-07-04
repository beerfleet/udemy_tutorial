class Robot:
    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        self.battery = battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"BeeP BOOP BLIP BLIP. I am {self.name}"
        return "Looooowwwww pppoooowwwwwerrrrrrrrr"

    def learn_skill(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skill)
            return f"MUHAHAHAHAHA, I acquired the skill of {new_skill.upper()}"
        return  "Insufficient battery, please charge a bit"