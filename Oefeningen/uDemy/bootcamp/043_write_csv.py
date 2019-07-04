from functools import wraps
from csv import reader, writer, DictReader, DictWriter


def try_function(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"********** {fn.__name__} ***********")
        resultaat = fn(*args, **kwargs)
        print(f"\n")
        return resultaat
    return wrapper


pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighters.csv'
doel = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighter_UPPER.csv'
moves = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighter_moves.csv'
doel2 = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/fighter_inches.csv'


@try_function
def simple_write(pad):
    # use newline='' to avoid writing extra whitelines (= windows bug)
    with open(pad, 'w', encoding='utf-8', newline='') as street_fighters:
        csv_writer = writer(street_fighters)
        csv_writer.writerow(['Character', 'Move'])
        csv_writer.writerow(['Ryu', 'Hadouken'])


@try_function
def read_to_write(source, target):
    with open(pad, 'r', encoding='utf-8') as lees_bestand:
        csv_reader = reader(lees_bestand)
        #lijst = list(csv_reader)
        with open(target, 'w', encoding='utf-8', newline='') as schrijf_bestand:
            csv_writer = writer(schrijf_bestand)
            for rij in csv_reader:
                csv_writer.writerow([el.upper() for el in rij])


@try_function
def write_dict(pad):
    with open(pad, 'w', encoding='utf-8', newline='') as moves_bestand:
        headers = ['Character','Move']
        moves_writer = DictWriter(moves_bestand, headers)
        moves_writer.writeheader()
        moves_writer.writerow({
            "Character": "Je mama",
            "Move": "Doe de afwas"
        })
        moves_writer.writerow({
            "Character": "Je mama",
            "Move": "Doe het eten"
        })
        moves_writer.writerow({
            "Character": "Je mama",
            "Move": "Huis kuisen"
        })


@try_function
def convert_to_inches(pad, doel2):
    convert = lambda x : float(x)/2.54
    with open(pad, encoding='utf-8') as fighters_in_cm:
        fighters_reader = DictReader(fighters_in_cm)
        with open(doel2, mode='w', encoding='utf-8', newline='') as fighters_in_inch:
            headers = ['Name','Country','Height (in cm)']
            fighters_writer = DictWriter(fighters_in_inch, headers)
            fighters_writer.writeheader()
            for fighter in fighters_reader:
                fighter.update({'Height (in cm)': convert(fighter['Height (in cm)'])})
                fighters_writer.writerow(fighter)


# simple_write(pad)
# read_to_write(pad, doel)
# write_dict(moves)
convert_to_inches(pad, doel2)