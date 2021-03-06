"""
Write a function called next_prime, which returns a generator that will 
yield an unlimited number of primes, starting from the first prime (2).
"""

def next_prime():
  
  def is_prime(getal):    
    return len([deler for deler in range(2, getal) if getal % deler == 0 ]) == 0

  prime = 2
  while True:
    if is_prime(prime):
      yield prime
      prime += 1
    else:
      prime += 1
    

primes = next_prime()
print([next(primes) for i in range(20)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
