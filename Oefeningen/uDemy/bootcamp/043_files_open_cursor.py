"""
Open file and read with cursor with seek()
"""

from functools import wraps


def scheid(naam):
    print(f"\n ********** {naam} ********** \n")


def decorate_file_io_demos(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        scheid(fn.__name__)
        resultaat = fn(*args, **kwargs)
        return resultaat
    return wrapper


@decorate_file_io_demos
def simpel_open():
    bestand = open(
        'C:/DEV/Python3/Oefenen/uDemy/bootcamp/open_file.txt', encoding="utf-8")
    inhoud = bestand.read()
    print(f"Lees bestand in: <<<< {inhoud if inhoud else '{}'} >>>> ")
    inhoud = bestand.read()
    print(
        f"Lees bestand nogmaals in: Inhoud ---- {inhoud if inhoud else '{}'} ---- want cursor is op het einde.")
    return bestand


@decorate_file_io_demos
def move_cursor_in_file(bestand):
    ''' Seek the n-th character in file, starting with 0 '''
    bestand.seek(0)
    inhoud = bestand.read()
    print(
        f"Na seek() Lees bestand in: ---- {inhoud if inhoud else '{}'} ---- ")
    return bestand


@decorate_file_io_demos
def lees_drie_lijnen(bestand):
    ''' Read the next line '''
    bestand.seek(0)
    lijn = bestand.readline()
    lijn = bestand.readline()
    print(f"Lijn 2 is : {lijn}")
    lijn = bestand.readline()
    print(f"Lijn 3 is : {lijn}")


@decorate_file_io_demos
def lees_lijnen_naar_lijst(bestand):
    bestand.seek(0)
    lijnen = bestand.readlines()
    return lijnen

@decorate_file_io_demos
def close_file(bestand):
    bestand.close()    
    return bestand

@decorate_file_io_demos
def is_file_closed(bestand):
    return bestand.closed

bestand = simpel_open()
move_cursor_in_file(bestand)
lees_drie_lijnen(bestand)
lijnen = lees_lijnen_naar_lijst(bestand)
print(f"Aantal lijnen : {len(lijnen)}")
print(close_file(bestand))
print(is_file_closed(bestand))