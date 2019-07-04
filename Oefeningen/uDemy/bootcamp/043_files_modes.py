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
def print_file_modes_to_file():
    with open('C:/DEV/Python3/Oefenen/uDemy/bootcamp/file_modes.txt', mode='a') as bestand:
        bestand.write("'r' : open file for reading (default).\n")
        bestand.write("'w' : open file for writing. Creates if non existing.\n")
        bestand.write("'x' : open file for excusive creation. Fails if file exists.\n")
        bestand.write("'r' : open file for appending at the end without truncating it. Creates new file, if does not exist.\n")
        bestand.write("'t' : open file in text mode (default).\n")
        bestand.write("'b' : open file in binary mode.\n")
        bestand.write("'+' : open file for updating (reading and writing.\n")

@decorate_file_io_demos
def add_r_plus():
    with open("C:/DEV/Python3/Oefenen/uDemy/bootcamp/write_r_plus.txt", mode='r+') as bestand:
        bestand.write(":)")
        bestand.seek(10)
        bestand.write(":(")

add_r_plus()

