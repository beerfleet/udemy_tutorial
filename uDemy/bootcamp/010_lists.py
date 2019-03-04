def scheid(tekst):
    print(f"\n ********* {tekst} *********** ")


def lijsten_intro():
    print("\n")
    lijst = ['1 kilo chillies',  '100 rollen wc-papier',  'liters bier',  9,  3.14,  True]
    scheid("Lijst info:")
    for item in lijst:
        print(f"Item ----- {item} ------ is een {type(item)}" )         
    scheid(f"Lijst lengte: {len(lijst)}")
    
    
def maak_lijst():
    lijst = range(1,  99)
    print(list(lijst))
    
    
def super_sentenced():
    scheid("Superzin")
    sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
    # Define your code below:
    result = ""
    for element in sounds:
        result += element.upper()
    print(result)
    

def lijst_append(lijst):
    scheid(" --- append() --- ")   
    scheid("Voeg 'Twee' toe")
    lijst.append('Twee')
    print(lijst)
    scheid("Voeg Lijst met 'Drie' en 'Vier' toe")
    lijst.append(['Drie',  'Vier']) 
    print(lijst)
    
def lijst_extend(lijst):
    scheid(" --- extend() --- ")
    lijst.extend([5,  6,  True,  'False'])
    print(lijst)
    scheid(f"Nieuwe lijst twee")
    lijst_twee = []
    scheid("Expand met alle elementen van lijst 1")
    lijst_twee.extend(lijst)
    print(lijst_twee)
    scheid("Wis lijst twee")
    lijst_twee.clear()
    print(lijst_twee)

def lijst_pop(lijst):
    scheid("Wis laatste element via INDEX")
    index = -1
    element = lijst.pop(index)
    print(f"index = {index} ; element = '{element}'")
    return element
    
def lijst_insert(lijst,  element):
    lijst.insert(0,  element)    
    print(f"Element {element} gaat naar begin : ",  end=" ")
    print(lijst)
    
def lijst_reverse(lijst):
    print("Keer lijst om: ", end=" ")
    lijst.reverse()
    print(lijst)
    
def lijst_remove(lijst):
    scheid("Wis laatste element met ingave van element zelf")
    lijst.remove(True)
    print(lijst)


def lijst_index(lijst):
    scheid(" --- lijst index posities op --- index(element, [start_index], [eind_index]) ")
    index = lijst.index(False)
    print(f"False bevindt zich in positie {index}")
    index = lijst.index(['Drie',  'Vier'])
    print(f"'[Drie,  Vier]' bevindt zich in positie {index}")
    lijst.insert(3,  'Een')
    print(lijst)
    index = lijst.index('Een', 4)
    print(f"Index van element 'Een',  vanaf index 4 te zoeken,  bevindt zich in {index}")
    # ValueError
    # index = lijst.index('Een', 4,  7)    
    # print(f"Index van element 'Een',  tussen index 4 en 7 te zoeken,  bevindt zich in {index}") 


def lijst_count(lijst):
    element = 'Een'
    aantal = lijst.count(element)
    scheid(f"Element '{element}' komt {aantal} keer voor in lijst") 
    
def lijst_join():
    scheid(" join() is a string method !!! ")
    lijst = ['Alfa',  'Papa',  'Tanga']    
    papatanga = " - papatanga -"
    ptjoin = papatanga.join(lijst)
    print(ptjoin)

def lijst_test():
    # Create a list called instructors
    instructors = []

    # Add the following strings to the instructors list 
        # "Colt"
        # "Blue"
        # "Lisa"
    instructors.extend(['Colt', 'Blue', 'Lisa'])

    # Remove the last value in the list
    instructors.pop()

    # Remove the first value in the list
    instructors.pop(0)

    # Add the string "Done" to the beginning of the list
    instructors.insert(0,  'Done')

    # Run the tests to make sure you've done this correctly!
    print(instructors)


def lijst_vergelijk():
    lijst_een = ['A',  'B',  'C']
    lijst_twee = ['A',  'B',  'C']
    lijst_drie = lijst_twee
    lijst_vier = lijst_een[:]
    lijst_zes = lijst_een[:1]
    lijst_zeven = [1,  2,  3,  4,  5,  6,  7]
    lijst_zeven_slice = lijst_zeven[::2]   
    print(f"Lijst 1 == lijst 2 ? {lijst_een == lijst_twee}")
    print(f"Lijst 1 is lijst 2 ? {lijst_een is lijst_twee}")
    print(f"Lijst 2 is lijst 3 ? {lijst_twee is lijst_drie}")
    print(f"Lijst 4 == lijst 1 ? {lijst_vier == lijst_een}")
    print(f"Lijst 4 is lijst 1 ? {lijst_vier is lijst_een}")    
    print(lijst_zes)
    print(lijst_zeven_slice)
    
    
def lijst_alle_naar_string(lijst):
    scheid(" -- Allen naar strings ---")
    string_lijst = [ str(element) for element in lijst]
    print(string_lijst)
    return string_lijst

def operaties():
    lijst = ['Een',  2.0,  2,  False]
    lijst_append(lijst)
    lijst_extend(lijst)    
    element = lijst_pop(lijst)
    lijst_insert(lijst,  element)
    lijst_reverse(lijst)
    lijst_remove(lijst)
    lijst_index(lijst)
    lijst_count(lijst)
    lijst_join()
    sorteerbare_lijst = lijst_alle_naar_string(lijst)
    sorteerbare_lijst.sort()
    print(sorteerbare_lijst)


operaties()




