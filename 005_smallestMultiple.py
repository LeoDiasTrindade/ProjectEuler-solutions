#! python3
'''Project Euler - Problem 5 (Leonardo Dias - 08/05/2020)
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def findEssentialsFactors():
    composts = [2]
    for number in range(3, MAX_SEQ+1):
        antecessor = 1
        for compost in composts:
            antecessor *= compost
        # If number is divisible by its antecessors, ignore it
        if antecessor%number == 0:
            continue
        # Else, add it and take off its factors
        else:
            for factor in composts:
                if number%factor == 0: del composts[composts.index(factor)]
            composts.append(number)
    return composts

def smallestMultiple(MAX_SEQ):
    composts = findEssentialsFactors()
    ans = 1

    for compost in composts:
        ans *= compost
    return ans

if __name__ == "__main__":
    MAX_SEQ = 20
    print(smallestMultiple(MAX_SEQ))
# ANSWER = 232792560
