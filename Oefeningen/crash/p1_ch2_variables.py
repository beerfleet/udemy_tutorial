'''
Created on 28 jan. 2019

@author: jvanbiervliet
'''

if __name__ == '__main__':
    pass

def main():
    boodschap = simple_message()
    uitvoer(boodschap)
    boodschap = wijzig_boodschap("NIETS MEER MEE TE MAKEN")
    uitvoer(boodschap)

def uitvoer(message):
    print (message)
    
def wijzig_boodschap(boodschap):
    return boodschap

def simple_message():
    message = "Een simpele boodschap"
    return message;

main()