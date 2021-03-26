#! python3
'''Project Euler - Problem 7 (Leonardo Dias - 11/05/2020)
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
'''


def prime(n):
    """ Return the n-th prime """
    number = 1
    for _ in range(n):
        number += 1
        while True:
            for antecessor in range(2, int(number**(1/2)) + 1):
                if number%antecessor == 0: number += 1; break
            else:
                break
    return number

if __name__ == '__main__':
    ORDER = 10001
    print(prime(ORDER))
# Answer = 104743
