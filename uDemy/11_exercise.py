'''
Created on 24 jan. 2019

@author: jvanbiervliet
'''

from operator import itemgetter

def collecteer_namen():
    namen = {}
    invoer = input('Geef een naam in of stop met - :')
    while invoer != '-':
        namen[invoer] = ''
        invoer = input('Geef nog een naam in of stop met - :')
    return namen

def geef_scores(namen):
    for i in namen:
        score = input('Geef de score van ' + i + ': ')
        namen.update({i: float(score)})        

def geef_top_drie(namen):
    student_tuples = namen.items();
    gesorteerd = sorted(student_tuples, key=itemgetter(1))
    aantal_leerlingen = len(gesorteerd)    
    top_drie = []
    for i in range(aantal_leerlingen-1, aantal_leerlingen-4,-1):
        top_drie.append(gesorteerd[i])                
        
    return top_drie
        
def toon_top_drie(top_drie):
    print ('Mijn drie beste leerlingen zijn:')
    print(top_drie)
    
def beloon_top_drie(top_drie):    
    print (' ----------- BELOON ------------')
    print('{} heeft {} verdiend.'.format(top_drie[0][0], '500€' ))
    print('{} heeft {} verdiend.'.format(top_drie[1][0], '300€' ))
    print('{} heeft {} verdiend.'.format(top_drie[2][0], '100€' ))

namen = {}
namen = collecteer_namen()
geef_scores(namen)
top_drie = geef_top_drie(namen)
toon_top_drie(top_drie)
beloon_top_drie(top_drie)

