'''
Created on 28 jan. 2019

@author: jvanbiervliet
'''
lijst = []

def bewaar_namen():
    return ['Jakke', 'Pjer', 'Inventao']

def druk_een_voor_een():
    print( lijst[0] )
    print( lijst[1] )
    print( lijst[2] )
    
def druk_met_boodschap():
    print ('Dit is een test ' + lijst[0])
    print ('Dit is een test ' + lijst[1])
    print ('Dit is een test ' + lijst[2])

lijst = bewaar_namen()
druk_een_voor_een()
druk_met_boodschap()