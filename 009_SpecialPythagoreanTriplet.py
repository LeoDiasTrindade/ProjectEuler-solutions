#! python3
'''	Project Euler - Problem 9 (Leonardo Dias - 11/05/2020)

	A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
		a² + b² = c²
	For example, 3² + 4² = 9 + 16 = 25 = 52.
	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.

'''

def isInt(var):
    try: var1=float(var); return True if var1==int(var1) else False
    except ValueError: return False

def PythagoreanTriplet():
    limSeq = 2
    gen = (lambda limSeq: ((a, b, (a**2 + b**2)**(1/2)) for a in range(1, limSeq) for b in range(1, limSeq-1)))
    while True:
        limSeq += 1
        nextGen = gen(limSeq)
        while True:
            try:
                while True:
                    a, b, c = next(nextGen)
                    if isInt(str(c)):
                        if (a+b+c == 1000): return a*b*c
            except StopIteration: break

if __name__=='__main__':
    print(int(PythagoreanTriplet()))

# Answer : 31875000 (375*200*425), 42s!!! (Corrigir)
