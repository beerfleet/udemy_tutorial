from random import randint

def geheim_paswoord():
    paswoord = 'Inagat'
    invoer = input("Wat is het geheime wachtwoord ? : ")
    while invoer != paswoord:
        print('Wachtwoord is niet correct :( ')
        invoer = input("Probeer opnieuw: ")
    print("Dat is correct !!")
    

def print_taco():
    for teller in range(0,  19):
        binnen_teller = 0
        while binnen_teller < teller:
            print("\U0001f600",  end=" ")
            binnen_teller += 1
        print(" ")


def stop_copying():
    zin = ""
    while zin != "stop met naapen":
        print(zin)
        zin = input(" -> ")
    print("OK JIJ WINT")
    

def voer_uit_tot_i_is_vijf():
    i = 0
    nummer = 0
    while nummer != 5:
        nummer = randint(1,  10)
        i += 1
    print(f"Het duurde {i} keer om 5 te genereren ... ")


def raad_getal_game():
    opnieuw = 'j'
    while opnieuw.upper() == "JA" or opnieuw.upper() == "J" :
        geheim_getal = randint(1,  10)
        raad_getal = 0        
        while raad_getal != geheim_getal:
            raad_getal = int(input("Raad een getal tussen 1 en 10: "))
            if raad_getal < geheim_getal:
                print("Geraden getal is te klein ... probeer opnieuw")
            elif raad_getal > geheim_getal:
                print("Geraden getal is te groot ... probeer opnieuw")
            else:
                break;
        print("Het geheim getal is inderdaad {}".format(geheim_getal))
        opnieuw = input("Wil je opnieuw spelen ? : ")
    

raad_getal_game()
