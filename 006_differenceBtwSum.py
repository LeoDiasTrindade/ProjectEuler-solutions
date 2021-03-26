#! python3
'''Project Euler - Problem 6 (Leonardo Dias - 08/05/2020)
    The sum of the squares of the first ten natural numbers is,
        1²+2²+...+10²=385
    The square of the sum of the first ten natural numbers is,
        (1+2+...+10)²=552=3025
    Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025−385=2640.
    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
'''


def difSquares():
    sum_sq, sq_sum = 0, 0

    for number in range(MAX_NUMBER+1):
        sum_sq += number ** 2
    for number in range(MAX_NUMBER+1):
        sq_sum += number
    return abs(sq_sum**2-sum_sq)

if __name__ == "__main__":
    MAX_NUMBER = 100
    print(difSquares())
# Answer = 25164150
