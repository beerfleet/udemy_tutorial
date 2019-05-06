from functools import wraps

def scheid(naam):
    print(f"\n ********** {naam} ********** \n")

def open_bestand(pad, access):
    try:
        bestand = open(pad, access, encoding='utf-8')
        return bestand
    except OSError as fout:        
        return fout.args[1]

def decorate_file_io_demos(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        scheid(fn.__name__)
        resultaat = fn(*args, **kwargs)
        return resultaat
    return wrapper

@decorate_file_io_demos
def schrijf_bestand(bestand, tekst):
    bestand.write(tekst)

with open('C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/poem.txt', 'w') as bestand:
    schrijf_bestand(bestand, 'De kat op de sofa ...\n')
    schrijf_bestand(bestand, 'Stomme kat, ga eraf!\n')
    schrijf_bestand(bestand, 'Haar in de lucht ...\n')