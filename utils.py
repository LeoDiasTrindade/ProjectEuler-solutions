class Utils:
    '''
    Organizar melhor essa classe depois
    Separar por utilidade talvez...'''

    # Primes

    def crive_Eratotenes(lim: int) -> None:
        '''Shows the max prime before n'''
        numbers = [True] * lim
        number, prime = 2, 2
        while number < lim:
            if numbers[number]:
                for i in range(0, lim, number):
                    numbers[i] = False
                    prime = number
            number += 1
        if number<=2: print("There's no prime under {}".format(lim))
        else:         print(prime)


    def isPrime(number: int) -> bool:
        '''Checks if a given number is prime'''
        if number<2: return False
        else:
            for i in range(2, number):
                if not number%i: return False
            else: return True


    def isPrime_recursion(number, inv=None) -> bool:
        '''Checks in a recursive way if a given number is prime'''
        if inv==None: inv = number
        if number<2: return False
        elif number==2: return True
        else:
            if inv%(number-1)==0: return False
            else: return isPrime_rec(number-1, inv)



    # Fibonacci

    def fibonacci_recursion(n, ans=1):
        # TODO
        pass

    def fibonacci(n: int):
        '''
        Return the n^th number of Fibonacci sequence'''
        current, sucessor = 0, 1
        for _ in range(n):
            current, sucessor = sucessor, current+sucessor
        return current


    def fibonacci_sequence(n: int):
        '''
        Return the sequence of Finonacci with n numbers'''
        current, sucessor = 0, 1
        sequence = []
        for _ in range(n):
            sequence.append(current)
            current, sucessor = sucessor, current+sucessor
        return sequence


    def generator_fibonacci(quantity: int):
        '''
        Return the sequence of Finonacci with n numbers'''
        current, sucessor = 0, 1
        for _ in range(quantity):
            current, sucessor = sucessor, current+sucessor
            yield current



    # factorial

    def factorial(number: int):
        ans = 1
        for i in range(1, number+1):
            ans *= i
        return ans


    def factorial_recursion(number: int):
        return 1 if number == 0 else number * factorial_rec(number-1)


    def tail_factorial(number: int, value=1):     # Avoid the stack overflow
        return value if number==0 else tail_factorial(number-1, number*value)



    # Pascal Triangle
    @staticmethod
    def pascals_triangle(n, ans=[]):
        '''Creates pascal triangle in a recursive way'''
        if ans==[]: ant=[1]
        else:
            ant = [1] + [ans[-1][i] + ans[-1][i-1] for i in range(1, len(ans[-1]))] + [1]
        ans.append(ant)
        if n: return Utils.pascals_triangle(n-1, ans)
        else: return ans

def main():
    # --------- Testes -----------

    print('{:^30}'.format('Test'))
    print('_'*30+'\n')

    Triangle = Utils.pascals_triangle(5)
    for row in Triangle:
        print(row)


if __name__=='__main__':
    main()
