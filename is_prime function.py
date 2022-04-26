import math
import numpy

def is_prime(number):
  if number == 2:
    return True
  if number > 1:
    for z in range(2, int(math.sqrt(number) + 1)):
      if ((number % z) == 0):
        #print number, ("is not prime")
        #print z, "times ", (number // z), "equals ", number
        return False
    else:
      return True
# Your "is_prime" function goes up here


number_of_primes = 0
for number in range(1,10**2):
  if number % 10**4 == 0:
    print number
  if is_prime(number):
    number_of_primes += 1
print number_of_primes