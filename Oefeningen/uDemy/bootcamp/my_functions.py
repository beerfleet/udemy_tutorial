import random

def genereer_lijst(start,  stop,  step):
    return [el for el in range(start,  stop,  step)]

def genereer_random_lijst():
    '''    Genereer een willekeurige lijst getallen    '''
    #lijst = [item for item in range(4)]
    start = random.randint(0,  100)
    stop = random.randint(start,  10000)
    step = random.randint(-50,  50)
    if step < 0:
        temp = start
        start = stop
        stop = temp
    lijst = genereer_lijst(start,  stop,  step if step != 0 else 1)
    return lijst
