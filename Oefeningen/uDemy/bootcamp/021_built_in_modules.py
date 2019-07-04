# from math import sqrt

# answer = sqrt(15129)
# print(answer)

from keyword import iskeyword


def contains_keyword(*kw):
    is_kw = False
    for word in kw:
        if iskeyword(word):
            is_kw = True
    return is_kw


print(contains_keyword("hello",  "lol",  'de'))
