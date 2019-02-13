from numpy.random.mtrand import randint

aantal_getallen = 6

def genereer_getal(bereik):
    return randint(1, bereik)

getallen = []

for i in range(0, aantal_getallen):
    getallen.append(genereer_getal(60))    
    
print(getallen)