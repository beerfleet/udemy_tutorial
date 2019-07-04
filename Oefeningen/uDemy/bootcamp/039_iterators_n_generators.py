def iteratewhore():
    name = "Janvanbiervliet"
    teller = iter(name)    
    for letter in teller:
        print(letter)

def custom_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        else:
            func(i)

def square(x):
    print (x*x)

if __name__ == "__main__":
    custom_for([1, 6, 9, 8, 77, 88], square)
    custom_for("LOL", print)