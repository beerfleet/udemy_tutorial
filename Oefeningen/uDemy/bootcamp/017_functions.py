import random

def scheid(msg):
    print(f"*************** {msg} ************* ")
    
def functies_intro():
    scheid('En nu naar de FUNCTIES')
    
def square(number):
    return print(number*number)
    
def flip_coin():
    coin = random.choice(range(2))    
    if coin == 0:
        print("It's heads")
    else:
        print("It's tails")
        
def generate_events():
    resultaat = [getal for getal in range(1, 50) if getal % 2 == 0]    
    return print(resultaat)

def yell(something):
    return ("{}!".format(something.upper()))
    
def default_param(number,  power = 2):
    return number**power
    
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
        
def no_order(first,  second):
    return f"{first},  {second}"
    
def print_order():
    scheid("Order")
    print(no_order(first="jan",  second="Pier"))
    print(no_order(second="Pier",  first="jan"))
    

instr = 'jan'
def say_hello():    
    return f'Hello {instr}'
    
def concat_hello():
    global instr
    instr += 'wakamole'
    return instr
    
def say_bye():
    instr = 'PETER'
    return f"Bye {instr}"
    
total = 99
def increment():
    global total
    total += 1
    return total    
    

print(concat_hello())
