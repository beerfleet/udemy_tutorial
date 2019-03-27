def oefening():
    uitvoer = ""
    for nummer in range(1,  21):
        if nummer == 4 or nummer == 13:
            uitvoer = f"{nummer} is ONGELUKSGETAL"
        elif nummer % 2 == 0:
            uitvoer = f"{nummer} is even"
        else:
            uitvoer = f"{nummer} is oneven"
        print(uitvoer)

oefening()
