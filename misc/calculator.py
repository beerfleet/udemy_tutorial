def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')
    
    number_1 = float(input('Geef eerste cijfer: '));
    number_2 = float(input('Geef tweede cijfer: '));
    
    if operation == '+':
        print('{} + {} = {} ' .format(number_1, number_2, number_1 + number_2))        
    elif operation == '-':
        print('{} - {} = {} ' .format(number_1, number_2, number_1 - number_2))
    elif operation == '*':
        print('{} * {} = {} ' .format(number_1, number_2, number_1 * number_2))
    else: 
        print('{} / {} = {} ' .format(number_1, number_2, number_1 / number_2))
    
    again()

def again():
    # Take input from user
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    
    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

calculate()