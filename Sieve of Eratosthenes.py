import math

N = 10 ** 3


def sieve(max_n):
    prime_dict = {1: False}
    for i in range(2, max_n + 1):
        prime_dict[i] = True

    for i in range(2, int(math.sqrt(max_n) + 1)):
        if prime_dict[i] == True:
            for m in range(2, (max_n / i) + 1):
                prime_dict[i * m] = False
    return prime_dict


sieve_count = 0

primes = sieve(N)
print "\nSieve Complete \n"
for z in primes:
    if primes[z]:
        sieve_count += 1

print str(sieve_count) + " is the number of primes between 1 and " + str(N) + "\n"
print "Here is the dictionary for all numbers between 1 and " + str(N)
print primes