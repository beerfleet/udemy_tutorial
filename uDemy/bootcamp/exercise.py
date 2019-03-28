import helpers

#num = helpers.lucky_number()
#print(num)

def generate_card_deck():
    deck = []
    for kleur in ("clubs",  "spades", "diamonds",  "hearts"):
        for waarde in range(1,  14):
            deck.append((waarde,  kleur))
    return deck
    
deck = generate_card_deck()
for kaart in deck:
    print(kaart)
