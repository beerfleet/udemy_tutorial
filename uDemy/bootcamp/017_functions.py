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
    
print(yell("een fles cola"))
