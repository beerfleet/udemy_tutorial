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
    
fibonacci()
