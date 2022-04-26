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


primes = sieve(N)
omg_twinziez = 0
for number in primes:
    if primes[number]:
        if number + 2 in primes:
            if primes[number + 2]:
                omg_twinziez += 1

print "The number of twin prime pairs between", 1, "and", N, "is", omg_twinziez