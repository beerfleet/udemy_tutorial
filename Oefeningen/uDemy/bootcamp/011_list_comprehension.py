def scheid():
    print("********************************")

def nums_demo():
    nums = [0,  1,  1,  2,  3,  5,  8,  13,  21,  34,  55,  89]
    print([chr(getal) for getal in nums])
    scheid()
    
def three_friends():
    friends = ['Aapren',  'Buccel',  'Concrio']
    print([friend[0].upper() for friend in friends])
    scheid()
    
def odd_even():
    reeks = range(1,  201)
    even = [num for num in reeks if num % 2 == 0]
    oneven = [num for num in reeks if num % 2 != 0]
    print(f'even nummers = {even}')
    print(f'oneven nummers = {oneven}')
    scheid()
    
def comprehension_exercises():
    the_list = ['Elie', 'Tim', 'Matt']
    answer = [name[0] for name in the_list]
    the_numbers = range(1,7)
    answer2 = [nr for nr in the_numbers if nr % 2 == 0]
    print(f"Answer 1 = {answer}")
    print(f"Answer 2 = {answer2}")
    scheid()
    list1 = range(1, 5)
    list2 = range(3, 7)
    answer3 = [nr for nr in list1 if nr in list2]
    list3 = ["Elie", "Tim", "Matt"]
    answer4 = [name[::-1].lower() for name in list3]
    print(f"Answer3 = {answer3}]")
    print(f"Answer4 = {answer4}]")
    scheid()
    
def div_by_twelve():
    numbers = range(1, 101)
    answer =  [nr for nr in numbers if nr % 12 == 0]    
    print(answer)
    
def no_vowels():
    vowels = ['a',  'e',  'i',  'o',  'u']
    answer = [character for character in 'amazing' if character not in vowels]
    print(answer)
    scheid()
    
def nested_comprehension():
    answer = [[num for num in range(10)] for lijst in range(10)]
    print(answer)
    scheid()

nums_demo()
three_friends()
odd_even()
comprehension_exercises()
div_by_twelve()
no_vowels()
nested_comprehension()
