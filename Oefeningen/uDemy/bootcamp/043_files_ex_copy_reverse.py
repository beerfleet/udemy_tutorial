'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

def copy_and_reverse(src_path, tgt_path):
    with open(src_path) as src_file:
        text = src_file.read()
    with open(tgt_path, 'w') as tgt_file:
        tgt_file.write(text[::-1])

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(path):
    with open(path, 'r') as bestand:
        lines = len(bestand.readlines())
        bestand.seek(0)
        words = len(bestand.read().split())
        bestand.seek(0)
        letters = len(bestand.read())
        return {'lines': lines, 'words': words, 'characters': letters}

# copy_and_reverse('C:/DEV/Python3/Oefenen/uDemy/bootcamp/story.txt', 'C:/DEV/Python3/Oefenen/uDemy/bootcamp/story_reversed.txt')

statistics('C:/DEV/Python3/Oefenen/uDemy/bootcamp/story.txt')