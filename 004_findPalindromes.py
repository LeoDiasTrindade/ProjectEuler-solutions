#! python3
'''Project Euler - Problem 4 (Leonardo Dias - 08/05/2020)
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
'''

def FindPalindrome(n_digits):
    gene = (i*j for i in range(10**(n_digits), 10**(n_digits-1), -1) for j in range(10**(n_digits), 10**(n_digits-1), -1))
    while True:
        number = str(next(gene))
        for index in range(len(number)//2):
            if number[index] != number[-(index+1)]: break
        else: break
    return number

if __name__ == '__main__':
    N_DIGITS = 3
    print(FindPalindrome(N_DIGITS))

# Answer = 580085
