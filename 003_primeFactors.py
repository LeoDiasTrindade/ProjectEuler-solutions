#! python3
''' Project Euler - Problem 3 (Leonardo Dias - 08/05/2020)

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?

'''

def primeFactor(number):
    prime = False
    factor = number

    while (factor > 1 and not prime):
        # Find the factors in decrease order
        if (number%factor == 0):
            # Inspect if the factor is or isn't a prime
            for i in range(2, int(factor ** (1/2))+1, 1):
                if factor%i == 0: factor /= i;  break
            else: prime = True
        else: factor -= 1
    return int(factor)

if __name__ == '__main__':
    NUMBER = 600851475143
    print(primeFactor(NUMBER))

# Answer = 6857
