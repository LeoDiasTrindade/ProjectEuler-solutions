''' Project Euler - Problem 14 (Leonardo Dias - 07/06/2020)

    The following iterative sequence is defined for the set of positive integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def quantity_terms_collazt_sequence(number=1, order=1):
    if number == 1:     return order
    elif number%2 == 0: return quantity_terms_collazt_sequence(number/2, order+1)
    else:               return quantity_terms_collazt_sequence(3 * number + 1, order + 1)


if __name__=='__main__':
    LIMIT = 1000000

    max_quantity_terms_for_num, num = 0, 1
    for i in range(1, LIMIT):
        if quantity_terms_collazt_sequence(i) > max_quantity_terms_for_num:
            max_quantity_terms_for_num = quantity_terms_collazt_sequence(i)
            num = i
    print(num)

# Answer: 837799 (it generates a sequence of 525 terms)
