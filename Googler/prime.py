import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

user_input = int(input("Upper Limit for prime:"))


for j in range(2,user_input+1):
    if is_prime(j):
        print(j)