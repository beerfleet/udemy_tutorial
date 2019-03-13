#!C:\Tools\Python\

def print_them(x):
    print (" **** ***** **** *** ** ** *")
    print(x)
    print(id(x))
    print(type(x))

def int_properties():    
    print_them(1)    
    print_them(2)
    print_them(1)    
    print(" --- x and y -----")
    x = 1
    y = 1
    print_them(x)
    print_them(y)
    print(x == y)
    print(x is y)
    
def float_properties():
    print("***** FLOAT ******")
    print_them(3)
    print_them(3 / 2)
    print_them(round(42 / 9))
    print_them(round(42 // 9))
    print_them(round(42 / 9,  3))
    print_them(round(42 % 7))
    print_them(int(34.78))
    print_them(float(23))

def main():
    print("--- object properties ---")
    int_properties()
    float_properties()
    
    
if __name__ == "__main__":    
    main()
