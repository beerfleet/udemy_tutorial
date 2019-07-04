'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''


def find_and_replace(pad_bestand, orig_woord, nw_woord):
    with open(pad_bestand, mode="r+", encoding='utf-8') as boek:
        tekst = boek.read()
        nw_tekst = tekst.replace(orig_woord, nw_woord)
        boek.seek(0)
        boek.write(nw_tekst)
        boek.truncate()


find_and_replace(
    'C:/DEV/Python3/Oefenen/uDemy/bootcamp/story.txt', 'Alice', 'Colt')
