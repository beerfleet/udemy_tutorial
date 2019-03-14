def test_sets():
    print("Sets are: \nimmutable, \nhave no duplicates, "
        +"\nhave no order,  \nhave no access by index"        
    )
    
def test_duplicate_in_set():
    a_set = ({4,  3,  2,  1,  4,  4})
    print(a_set)
    
def set_creation():
    print("First way: s = set({1, 2, 3}) ")
    s = set({1, 2, 3})
    print(s)
    print("Second way: s = set({1, 2, 3}) ")
    s2 = {1, 2, 3}
    print(s2)
    print(s == s2)
    print(s is s2)
    
def set_order():
    print("** ** *** *** Now for wome order")
    s = {1,  2, 99, 3.14, '3.14', 0x145,  False}
    for item in s:
        print(item)
        
def de_double():
    lijst = ['Jan',  'Paola',  'Betty',  'Jan',  'Betty',  'Paola',  'Betsy',  'Bettie',  'João',  'John',  'Jan']
    enkels = set(lijst)
    print(enkels)
    unieke_lijst = list(enkels)
    unieke_lijst.sort()
    print (unieke_lijst)

def set_add():
    s = {1, 2, 3}
    s.add(99)
    print(s)
    
def set_math():
    set1 = {1, 2, 3}
    set2 = {2, 4, 6}
    set3 = set1 & set2 # set3 = set1.intersection(set2)
    print(f"Set 1 = {set1},  Set 2 = {set2}")
    print ("Union = {}".format(set1 | set2))
    print("Intersection = {}".format(set3))

def sets_test_ex():
    # 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
    numbers = (1, 2, 3, 4)
    # 2 - Create a variable called value which is a tuple with the the value 1 inside.
    value = (1, )
    # 3 - Given the following variable:
    values = [10,20,30]
    # Create a variable called static_values which is the result of the values variable converted to a tuple
    static_values = tuple(values)
    # 4 - Given the following variable
    stuff = [1,3,1,5,2,5,1,2,5]
    # Create a variable called unique_stuff which is a set of only the unique values in the stuff list
    unique_stuff = set(stuff)
    
    print(type(numbers))
    print(type(value))
    print(type(static_values))
    print(unique_stuff)
    print(type(unique_stuff))
    
sets_test_ex()
