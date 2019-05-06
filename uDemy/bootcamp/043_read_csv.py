from functools import wraps
from csv import reader, DictReader

def try_function(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"********** {fn.__name__} ***********")
        resultaat = fn(*args, **kwargs)
        print(f" ----    ----    ----")
        return resultaat
    return wrapper

@try_function
def do_not_do_this(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        print(fighters_file.read())

@try_function
def csv_reader(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        csv_reader = reader(fighters_file)
        for row in csv_reader:
            print(row)

pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighters.csv'
do_not_do_this(pad)
csv_reader(pad)
