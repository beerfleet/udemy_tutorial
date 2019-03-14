def intro_sets_compreh():
    print(' \n****************** This will introduce sets comprehension')
    
def for_x_in_range():
    set1 = {x*x for x in range(10)}
    print(set1)
    dict = {x:x*x for x in range(10)}
    print(dict)
    list = [x for x in range(10)]
    print(list)
    set2 = { x*x for x in range(30) }
    set3 = {chr(x) for x in set2}
    print(f"Set 3 = {set3}")
    
def define_string():
    return "azeezeferu"

def analyse(string):
    return {char for char in string if char in 'aeiou'}

def execute():
    mijn_str = define_string()
    length_is_five = len(analyse(mijn_str)) == 5    
    print(length_is_five)

execute()
