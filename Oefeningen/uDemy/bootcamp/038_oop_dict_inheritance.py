class GrumpyDict(dict):
    def __repr__(self):
        return f"{super().__repr__()}, also: Fuck off"

if __name__ == "__main__":

    d = dict()
    gd = GrumpyDict({"first": "John", "last": "Doe"})
    print(gd)