#! python3
#  Answer = 4613732

def fibEven(limit):
    current, next = 0, 1
    while current <= limit:
        if current%2 == 0: yield current
        current, next = next, current+next

if __name__ == '__main__':
    LIMIT = 4e6
    print(sum(fibEven(LIMIT)))
