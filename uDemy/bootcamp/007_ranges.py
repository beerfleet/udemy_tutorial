def print_lijst():
    bereik = range(0,  64,  3)
    lijst_op = list(bereik)
    print(lijst_op)

def blok_tafels():
    for horizontaal in range(1, 11):
        for verticaal in range (1,  11):
            product = horizontaal * verticaal
            str_product = str(product)
            print(str_product.rjust(3), end=" ")
        print('\n')
        
blok_tafels()
