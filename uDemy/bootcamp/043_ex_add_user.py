from csv import writer, reader

pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/users.csv'


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

if __name__ == "__main__":
    # add_user('Jan', 'Bier')
    print_users()