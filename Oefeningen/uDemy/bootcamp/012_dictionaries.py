def scheid():
    print("********************************")
    
def dictionary_creation():
    user_info = {'name': 'Jefklak', 'age': 29, 'sex': 'male'}
    print(user_info)
    scheid()

def access_dictionary():    
    artist = {
        "first": "Neil",
        "last": "Young",
    }
    full_name = artist['first'] + ' ' + artist['last']
    print(f"Volledige naam = {full_name}")
    scheid()

def calculate_donations():
    # DON'T TOUCH PLEASE!
    donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
    # DON'T TOUCH PLEASE!
    total_donations = 0
    for value in donations.values():
        total_donations += value
    # Use a loop to add together all the donations and store the resulting number in a variable called total_donations
    print("Totaal donaties = {}".format({total_donations})) 
    
def access_fromkeys():
    # This code picks a random food item:
    from random import choice #DON'T CHANGE!
    food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

    #DON'T CHANGE THIS DICTIONARY EITHER!
    bakery_stock = {
        "almond croissant" : 12,
        "toffee cookie": 3,
        "morning bun": 1,
        "chocolate chunk cookie": 9,
        "tea cake": 25
    }

    # YOUR CODE GOES BELOW:
    if food in bakery_stock:
        print("{} left".format(bakery_stock[food]))
    else:
        print("We don't make that")
        
    print(food)
    scheid()
    
def init_properties():
    #DO NOT TOUCH game_properties!
    game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

    # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
    initial_game_state = dict.fromkeys(game_properties,  0)
    for stat in initial_game_state.items():
        print(str(stat))
    scheid()
        
def exercises():
    inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
    # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
    stock_list = dict.copy(inventory)

    # add the value 18 to stock_list under the key "cookie"
    stock_list.update({'cookie': 18})

    # remove 'cake' from stock_list USE A DICTIONARY METHOD
    stock_list.pop('cake')
    print(stock_list)

    
dictionary_creation()
access_dictionary()
calculate_donations()
access_fromkeys()
init_properties()
exercises()
