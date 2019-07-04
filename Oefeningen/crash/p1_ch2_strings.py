'''
Created on 28 jan. 2019

@author: jvanbiervliet
'''

# oef 2-3
naam = ''

def invoer_naam(naam):
    return naam

def print_boodschap(naam):
    print ("Wie hebben baarden ? {}".format(naam))

# oef 2-4
def print_cases(naam):
    print('In kleine letters = {}'.format(naam.lower()))
    print('In hoofdletters = {}'.format(naam.upper()))
    print('In kleine letters = {}'.format( naam.title() ))
    
# oef 2-5
def print_quote(quote):
    print('\t' + quote)
    
# oef 2-7
def naam_stripper(naam):
    print ("Naam gewoon: {}".format(naam))
    print ("Naam R strip: {}".format(naam.rstrip()))
    print ("Naam L strip {}".format(naam.lstrip()))    
    print ("Naam strip {}".format(naam.strip()))    

def strippers():
    naam_stripper('\tJan\n')
    naam_stripper('\nJan\t')
    naam_stripper('\tJan\t')
    naam_stripper('\nJan\n')
    naam_stripper(' Jan ')
    naam_stripper(' Jan\n')
    naam_stripper(' Jan\t')
    naam_stripper('\tJan ')

print ("Oef 2-3")
naam = invoer_naam('Jan Pier Tjoris en Corneel')
print_boodschap(naam)

print ("\nOef 2-4")
print_cases(naam)

print ("\nOef 2-5")
print_quote("De gustibus et colorebus non disputandem -- dad")

print ("\nOef 2-7")
strippers()
