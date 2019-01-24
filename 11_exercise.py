'''
Created on 24 jan. 2019

@author: jvanbiervliet
'''

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
        namen.update({i: int(score)})        

names = {}
names = collecteer_namen()
geef_scores(names)

print(names)