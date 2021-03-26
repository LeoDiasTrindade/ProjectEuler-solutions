#! python3
#  Answer = 233168

LIMIT = 1000

def sumMultiples():
    ans = sum(number for number in range(LIMIT) if (number%3==0 or number%5==0))
    return ans

if __name__ == "__main__":
    print(sumMultiples())
