class Train():

    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars

if __name__ == "__main__":
    train = Train(59)
    print(train)
    print(len(train))