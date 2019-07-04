'''
Created on 13 feb. 2019

@author: jvanbiervliet
'''

def test_loop():
    print('\n\n********************** Een test ***********************************')
    for letter in "Wat is een beerdiertje ?":
        print(letter, end=' ')


def fibonacci():
    print('\n\n********************** Fibonacci sequence *************************')
    bereik = int(input("Geef een getal in: "))
    fib = 0
    volgende = 1   
    for getal in range(0,  bereik + 1):
        print("Volgnummer = {}, fibonacci = {}".format(getal,  fib))
        tmp = fib + volgende
        fib = volgende
        volgende = tmp
    

def loop_and_range_exercise():
    x = 0
    for nummer in range(11,  21,  2):
        x += nummer
    print("De som van alle oneven getallen tussen 10 en 20 (inbegrepen) is {}".format(x))
    
    
def repeater_exercise():
    aantal_keer = int(input('Hoeveel keer ... ? : '))
    for i in range(1,  aantal_keer + 1):
        print(i)
        
repeater_exercise()
