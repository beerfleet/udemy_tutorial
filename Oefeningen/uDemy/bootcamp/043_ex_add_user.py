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
    with open(pad_thuis, 'r', encoding='utf-8', newline='') as bestand:
        bestand_lijnen = reader(bestand)
        users_updated = 0
        pers_lijst = list(bestand_lijnen)
        for persoon in pers_lijst:
            if persoon[0] == o_vnaam and persoon[1] == o_anaam:
                persoon[0], persoon[1] = n_vnaam, n_anaam
                users_updated += 1
    with open(pad_thuis, 'w', encoding='utf-8', newline='') as csv_bestand:
        schrijver = writer(csv_bestand)
        schrijver.writerows(pers_lijst)

    return "Users updated: {}.".format(users_updated)

""" OPLOSSING UDEMY
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)
"""



'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(vnaam, anaam):
    with open(pad_thuis) as csv_bestand:
        csv_lezer = reader(csv_bestand)
        rijen = list(csv_lezer)    
    
    with open(pad_thuis, 'w', encoding='utf-8', newline='') as csv_bestand:
        csv_schrijver = writer(csv_bestand)
        rijen_weg = 0
        for rij in rijen:
            if rij[0] != vnaam and rij[1] != anaam:
                csv_schrijver.writerow(rij)
            else:
                rijen_weg += 1
        return "Users deleted: {}.".format(rijen_weg)


if __name__ == "__main__":
    # add_user('Jan', 'Bier')
    # print_users()
    # print(find_user("Chaka", "Zulu"))
    # print(update_users("Colt", "Steele", "HELLO", "WORLD"))
    print(delete_users("Grace", "Hopper"))