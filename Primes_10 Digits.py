import math

N = 9999999999


def is_prime(number):
    if number == 2:
        return True
    if number > 1:
        for z in range(2, int(math.sqrt(number) + 1)):
            if ((number % z) == 0):
                # print number, ("is not prime")
                # print z, "times ", (number // z), "equals ", number
                return False
        else:
            return True


# largest_10digit_int = []
while N > 1000000000:
    if is_prime(N) == True:
        # largest_10digit_int.append(N)
        print "The smallest 10 digit prime is:", N
        break
    else:
        N -= 1

# print "The smallest ten digit number is:"
# print largest_10digit_int



