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

def toon_top_drie(namen):
    student_tuples = namen.items();
    gesorteerd = sorted(student_tuples, key=itemgetter(1))
    aantal_leerlingen = len(gesorteerd)
    print ('Mijn drie beste leerlingen zijn:')
    for i in range(aantal_leerlingen-1, aantal_leerlingen-4,-1):        
        print (gesorteerd[i])


namen = {}
namen = collecteer_namen()
geef_scores(namen)
toon_top_drie(namen)

