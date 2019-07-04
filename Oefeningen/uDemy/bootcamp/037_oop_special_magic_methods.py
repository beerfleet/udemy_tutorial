class Human():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __mul__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Integer please !!!")
        return [Human(self.first, self.last, self.age) for i in range(amount)]

if __name__ == "__main__":
    hue = Human("Bart", "Simpson", 8)
    print(hue)
    print(len(hue))
    humans = hue * 5
    humans[2].first = "Jane"
    print(humans)