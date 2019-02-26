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
    
    
stop_copying()
