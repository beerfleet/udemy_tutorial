import sys
import statistics
# import my_functions

def toon_functionaliteit():
    # print(sum.__doc__)
    return dir(sum)
    #help(random)    

def function_all():
    #lijst = genereer_random_lijst()
    people = ['Jahhny',  'Kaas',  'Marina',  'Tina',  'Albert',  'Jefklak']
    return all('a' in pers.lower() for pers in people)

# print(function_all())

def list_vs_generator():
    list_comp = sys.getsizeof([x * 10 for x in range(1000)])
    gen_exp = sys.getsizeof(x * 10 for x in range(1000))
    return(f"list {list_comp} ; generator {gen_exp}")

# print(list_vs_generator())    

def is_all_strings(lijst):
    return all(isinstance(s,  str) for s in lijst)

#♥ print(is_all_strings(['a',  'b',  'josee',  '0']))

def get_songs():
    return  [
        {"title": "happy b-day",  "playcount": 1}, 
        {"title": "Survive",  "playcount": 6}, 
        {"title": "YMCA",  "playcount": 99}, 
        {"title": "Toxic",  "playcount": 31}
    ]

def sort_by_playcount():
    songs  =get_songs()
    return(sorted(songs,  key=lambda s: s["playcount"],  reverse=True))
    
# print(sort_by_playcount())

def least_played():
    songs = get_songs()
    return min(songs,  key=lambda s: s["playcount"])

# print(least_played())

def longest_title():
    songs = get_songs()
    return max(songs,  key=lambda s: len(s["title"]))

# print(longest_title())    

def title_of_most_played():
    songs = get_songs()
    return max(songs,  key=lambda s: s["playcount"])["title"]

# print(title_of_most_played())

def extremes(rij):
    return (min(rij), max(rij))

# print(extremes([1,  99,  8,  -45]))

def max_magnitude(rij):    
    return abs(max(rij,  key=lambda n: abs(n)))
    
# print(max_magintude([300, 20, -900]))

def sum_even_values(*getallen):
    return sum(getal for getal in getallen if getal % 2 == 0) #if any(True for el in list(getallen) if el % 2 == 0) else 0
        
# print(sum_even_values(1,  7,  9,  13,  99,  1))

def sum_floats(*args):
    return sum(el for el in args if isinstance(el,  float))
    
# print(sum_floats(1,2,3,4,5))

def scores():
    midterms = [80,  91,  78]
    finals = [98,  89,  53]
    students = ['dan',  'ang',  'kate']
    final_grades = {trio[0]:statistics.mean([trio[1],  trio[2]]) for trio in zip(students,  midterms,  finals)}
    return final_grades
    
# print(scores())
    
def names_and_scores():
    midterms = [80,  91,  78]
    finals = [98,  89,  53]
    students = ['dan',  'ang',  'kate']
    return zip(students, map(lambda pair: max(pair),  zip(midterms,  finals)))
    
# print(dict(names_and_scores()))
    
def interleave(str1,  str2):
    lst = [it for it in zip(str1,  str2)]
    concat_str = ''
    for li in lst:
        for t in li:
            concat_str += t
    return concat_str
    
print((interleave('lzr',  'iad')))

def triple_and_filter(lijst):
    return list(map(lambda triple: 3*triple,  filter(lambda div_by_four: div_by_four % 4 == 0,  lijst)))
    
# print(triple_and_filter([6, 8, 10, 12]))

def extract_full_name(list_of_dict):        
    return [''.join(d['first'] + ' ' + d['last']) for d in [el for el in list_of_dict]]
    
#print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}, {'first': 'Abe', 'last': 'Burnes'}, {'first': 'Pierce', 'last': 'Dorothy'}]))
