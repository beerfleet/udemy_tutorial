'''
Created on 6 feb. 2019

@author: jvanbiervliet
'''

player1 = ""
player2 = ""

player1 = input("Player1, choose (r)ock, (p)aper, (s)cissors: ")
for i in range(0, 100):
    print(" * * * * * * * * * * *")    
player2 = input("Player2, choose (r)ock, (p)aper, (s)cissors: ")

win_text = ""

if player1 == 'r':
    win_text = "Player 1 chose rock.. "
    if player2 == 'p':
        win_text += "Player 2 wins !!!"      
    else:
        win_text += "Player 1 wins !!!"
elif player1 == 'p':
    win_text = "Player 1 chose paper.. "
    if player2 == 'r':
        win_text += "Player1 wins !!!"
    elif player2 == 's':
        win_text += "Player 2 wins !!!"
elif player1 == 's':
    win_text = "Player 1 chose scissors.. "
    if player2 == 'r':
        win_text += "Player 2 wins !!!"
    elif player2 == 'p':
        win_text += "Player1 wins !!!"
elif player1 == player2:
    win_text = "it\'s a tie"
else:
    win_text = "Invalid choice !!!!!"
        
print(win_text)
    