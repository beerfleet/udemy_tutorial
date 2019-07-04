from functools import wraps

def scheid(naam):
    print(f"\n ********** {naam} ********** \n")

def open_bestand(pad):    
    try:
        bestand = open(pad, encoding='utf-8')
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
def lees_een_lijn(bestand):
    return bestand.readlines()

@decorate_file_io_demos
def open_with():
    with open('C:/DEV/Python3/Oefenen/uDemy/bootcamp/open_file.txt') as bestand:
        print(bestand.readline())
    return bestand.closed

bestand = open_bestand('C:/DEV/Python3/Oefenen/uDemy/bootcamp/open_file.txt')
print(open_with())