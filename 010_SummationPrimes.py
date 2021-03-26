#! python3
'''Project Euler - Problem 10 (Leonardo Dias - 11/05/2020)
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
'''

def sumPrime(limit):
    ans = 0
    prime = 2
    while prime<limit:
        ans+=prime
        prime+=1
        while True:
            for i in range(2, int(prime**(1/2))+1):
                if prime%i==0: prime+=1; break
            else: break
    return ans

if __name__=='__main__':
	LIMIT = 2e6
	print(sumPrime(LIMIT))
# Answer: 142913828922
