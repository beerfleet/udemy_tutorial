def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

def yes_or_no():
    answer = 'no'
    while True:
        if answer == 'yes':
            answer = 'no'
            yield 'no'
        else:
            answer = 'yes'
            yield 'yes'


""" for day in week():
    print(day) """

""" aye_nayer = yes_or_no()
for i in range(99000):
    print(next(aye_nayer)) """

def make_song(count=99, beverage='soda'):
    while count >= 0:
        if count == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        elif count == 0:
            yield "No more {}!".format(beverage)
        else:
            yield "{} bottles of {} on the wall.".format(count, beverage)
        count -= 1

""" kombucha_song = make_song()
for verse in kombucha_song:
    print(verse) """

def get_multiples(number=1, count=10):    
    teller = 1
    while teller <= count:
        yield number * teller
        teller += 1

""" gen = get_multiples()
for el in gen:
    print(el) """

def get_unlimited_multiples(number = 1):
    add = number
    while True:
        yield number
        number += add

ones = get_unlimited_multiples(7)
for i in range(15):
    print(next(ones))