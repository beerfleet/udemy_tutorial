'''
Created on 30 jan. 2019

@author: jvanbiervliet
'''

getalA = None
getalB = None

def lees_getal_in():
    return int(input("Lees getal in: "))
    
def test_me(a,b):
    print("Invoer = {} en {}".format(a,b))
   
def lijst_delers(getal):    
    lijst = []
    for i in range(0, getal):
        deler = i + 1
        if getal % deler == 0:
            lijst.append(deler)
    return lijst

getalA = lees_getal_in()
getalB = lees_getal_in()

delersA = lijst_delers(getalA)
delersB = lijst_delers(getalB)
print (delersA)
print (delersB)
