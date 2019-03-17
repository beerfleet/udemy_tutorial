'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''

def return_day(index):
    day = dict({1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'})
    if index in day:
        return day.get(index)    
    return None

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(lijst):
    if len(lijst) <= 0:
        return None
    return lijst[-1]


'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a,b):
    if a == b:
        return "Numbers are equal"
    if a < b:
        return "Second is greater"
    return "First is greater"
    
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def  single_letter_count(tekst,  letter):
    aantal = 0
    for ltr in tekst:
        if ltr.lower() == letter:
            aantal+=1
    return aantal

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(tekst):
    counts = {ltr:tekst.count(ltr) for ltr in tekst}
    return counts

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(lijst,  operator,  positie,  getal = 0):
    if operator == "remove":
        if positie == "begin":
            return lijst[0]
        elif positie == "end":
            return lijst[-1]
    elif operator == "add":
        if positie == "begin":
            lijst.insert(0,  getal)
            return lijst
        elif positie == "end":
            lijst.append(getal)
            return lijst
    
'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(woord):
    palindroom_letter_lijst = [letter for letter in woord[::-1] if letter != " "]
    woord_letter_lijst = [letter for letter in woord if letter != " "]    
    palindroom_str = ''.join(palindroom_letter_lijst)
    woord_str = ''.join(woord_letter_lijst)
    return palindroom_str == woord_str
    
'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(lijst,  zoekterm):
    return lijst.count(zoekterm)
    
'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst): 
    total = 1
    if len([item for item in lst if item % 2 == 0]) == 0:
        total = 0
    for number in lst:        
        if number % 2 == 0:
            total = total * number
    return total

#print(multiply_even_numbers([1, 3, 999, 77])) # 48

def capitalize(tekst):
    print("TETTE")
    
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
