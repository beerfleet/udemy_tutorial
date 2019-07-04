def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I am {name}"

@shout
def insult(insult1, insult2, name='No One'):
    return f"{insult1}, you little {insult2}, {name}"

print(greet("Jozefien"))

print(insult("F* you", "Ahole", name="Pat"))