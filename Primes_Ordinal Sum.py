#This code takes the number under "N" and adds up all the prime numbers within 1 and N
import math

N = 100

def sieve(max_n):
    prime_dict = {1: False}
    for i in range(2, max_n + 1):
        prime_dict[i] = True

    for i in range(2, int(math.sqrt(max_n) + 1)):
        if prime_dict[i] == True:
            for m in range(2, (max_n / i) + 1):
                prime_dict[i * m] = False
    return prime_dict


ordinal_list = []
prime_dict2 = sieve(N)

for number in prime_dict2:
    if prime_dict2[number] == True:
        ordinal_list.append(number)
    elif len(ordinal_list) == 100000:
        break
ordinal_sum = sum(ordinal_list)
print "\n"
print ordinal_sum