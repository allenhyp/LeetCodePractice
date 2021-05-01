from collections import deque
def generateNumberUtil(MAX_COUNT):
    q = deque(['1'])
    for _ in range(MAX_COUNT):
        temp = q.pop()
        yield temp
        q.appendleft(temp + '0')
        q.appendleft(temp + '1')


def NonzeroMultiple(n):
    '''
    Find the smallest nonzero multiple M of n, while M can only contain 0 and 1.
    '''
    if n == 1: return '1'
    for candidate in generateNumberUtil(100):
        if int(candidate) % n == 0:
            return candidate
    return -1


if __name__ == '__main__':
    print(NonzeroMultiple(3))
