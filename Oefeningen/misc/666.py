def is_prime(number):    
    if number in (1, 2):
        return True
    counter = 2
    while counter < number:
        if number % counter == 0:
            return False
        counter += 1
    return True

def get_primes_from(number):
    priemen = [nr for nr in range(1, number) if is_prime(nr)]
    return priemen

def count_primes(number):
    return len(get_primes_from(number))

print(get_primes_from(666))
print(count_primes(666))