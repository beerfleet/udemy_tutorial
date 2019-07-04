# OFWEL gebruik onderstaande in console
# python -m doctest -v [filename]
# -------------------------------------

import doctest

def add(a, b):
    """
    >>> add(99, 1)
    100
    >>> add(-99, 98)
    -1
    """
    return a + b

# voorbeeld 2
def double(x):
    """
    >>> double(50)
    100
    >>> double(-1)
    -2
    """
    return 2*x

# OFWEL gebruik onderstaande + de import statement
if __name__ == "__main__":
    doctest.testmod()
#-------------------------------------------------