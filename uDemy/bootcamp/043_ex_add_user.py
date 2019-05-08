from csv import writer, reader

pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/users.csv'
pad_thuis = 'C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/users.csv'


def add_user(first, last):
    with open(pad, mode='a', encoding='utf-8', newline='') as gebruikers:
        schrijver = writer(gebruikers)
        schrijver.writerow([first, last])


def print_users():
    with open(pad, newline='') as gebruikers_file:
        lezer = reader(gebruikers_file)
        next(lezer)
        for persoon in lezer:            
            print("{},{}".format(persoon[0], persoon[1]))


def find_user(voornaam, achternaam):
    with open(pad_thuis, mode='r', encoding='utf-8') as bestand:
        lezer = reader(bestand)
        rij_teller = 0
        for row in lezer:            
            if row[0] == voornaam and row[1] == achternaam:
                return rij_teller
            rij_teller += 1
        return "{} {} not found.".format(voornaam, achternaam)

def update_users(o_vnaam, o_anaam, n_vnaam, n_anaam):
    with open(pad_thuis, 'w+', encoding='utf-8', newline='') as bestand:
        bestand_lijnen = bestand.readlines()
        print(bestand_lijnen)


if __name__ == "__main__":
    # add_user('Jan', 'Bier')
    # print_users()
    # print(find_user("Chaka", "Zulu"))
    update_users("Colt", "Steele", "Hello", "World")