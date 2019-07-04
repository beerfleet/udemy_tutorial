from functools import wraps
from csv import reader, DictReader


def try_function(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"********** {fn.__name__} ***********")
        resultaat = fn(*args, **kwargs)
        print(f"\n")
        return resultaat
    return wrapper


@try_function
def do_not_do_this(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        print(fighters_file.read())


"""
reader accepts delimiter:
csv_reader = reader(file, delimiter='|')
"""
@try_function
def csv_reader_per_row(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        csv_reader = reader(fighters_file)  # use reader() to create iterator
        next(csv_reader)  # skip headers
        for row in csv_reader:
            print(row)


@try_function
def csv_reader(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        csv_reader = reader(fighters_file)  # use reader() to create iterator
        next(csv_reader)  # skip headers
        for fighter in csv_reader:
            print(f"{fighter[0]} is from {fighter[1]}")


@try_function
def csv_reader_as_list(pad):
    with open(pad, encoding='utf-8') as fighters_file:
        csv_reader = reader(fighters_file)
        data = list(csv_reader)
        print(data)


@try_function
def csv_dictreader(pad):
    with open(pad, encoding='utf-8') as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            print(row['Name'])


pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighters.csv'
do_not_do_this(pad)
csv_reader_per_row(pad)
csv_reader(pad)
csv_reader_as_list(pad)
csv_dictreader(pad)
