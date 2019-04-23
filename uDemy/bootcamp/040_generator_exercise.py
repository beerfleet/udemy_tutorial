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

aye_nayer = yes_or_no()
for i in range(99000):
    print(next(aye_nayer))