'''
word occurences in story.txt
'''
import re

def count_occurence(word, text):
    word_list = text.split(' ')
    return len([w for w in word_list if w == word])


def lees_tekst_in(pad):
    woorden_counter = {}
    with open(pad, encoding='utf-8', mode='r') as bestand:
        tekst_lijst = re.findall(r"[\w']+", bestand.read().lower())
    for woord in tekst_lijst:
        if not woord in woorden_counter:
            woorden_counter[woord] = 0
        else:
            woorden_counter[woord] += 1
    return woorden_counter


if __name__ == "__main__":    
    pad = 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/docs/story.txt'
    pad_thuis = 'C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/story.txt'
    woorden_teller = lees_tekst_in(pad_thuis)
    with open('C:/DEV/Python_code/udemy_tutorial/uDemy/bootcamp/docs/story_results.txt', mode='a', encoding='utf-8') as resultaten:
        for k,v in sorted(woorden_teller.items(), key=lambda kol_twee: kol_twee[1], reverse=True):
            resultaten.write(f"{k}:{v}\n")
            #  print(k, v)

