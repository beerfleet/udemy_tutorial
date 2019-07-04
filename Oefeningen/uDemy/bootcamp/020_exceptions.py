def test_ex(letter):    
    if not (ord(letter) in range(ord('a'),  ord('z')) or ord(letter) in range(ord('A'),  ord('Z'))):
        raise ValueError('invalid char')        
    return letter
        
try:
    num = int(input("Geef een getal in "))
except:
    print("Not a number")
else:
    print("Correcte invoer, doe verder")
finally:
    print("wordt soieso uitgevoerd")
