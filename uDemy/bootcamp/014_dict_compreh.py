def dict_maak():    
    return dict(een= "een",  twee= "twee",  drie= "drie")
    #return dict(een= "een",  twee= "twee",  drie= "drie")
    
def lijst_maak():
    return [0,  1,  1,  2,  3,  5,  8,  13,  21,  34,  55] 
    
def dict_comprehension_syntax():
    woordenboek = dict_maak()
    som = sum([item for item in woordenboek.values()])                
    print(som)
    
def som_lijst(lijst):
    return sum(lijst)
    
def woordenboek_uit_lijst():
    lijst = lijst_maak()
    woordenboek = {item: item*item for item in lijst}
    print (woordenboek)
    
def upper_case():
    woorden = dict_maak()
    woorden_groot = {k: v.upper() for k, v in woorden.items()}
    print(woorden_groot)
    
def maak_vierkw_met_lijst():    
    vierk_dict = {nummer:nummer*nummer for nummer in range(0,  55) }
    print(vierk_dict)
    
def exercise():
    list1 = ["CA", "NJ", "RI"]
    list2 = ["California", "New Jersey", "Rhode Island"]
    # make sure your solution is assigned to the answer variable so the tests can work!
    #answer = {list1[list1.index(item)]: list2[list1.index(item)] for item in list1}
    answer = { list1[i]:list2[i] for i in range(3) }
    print(answer)
    
def convert_to_dic():
    person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
    answer = { kv[0]:kv[1] for kv in person}
    print (answer)

convert_to_dic()
