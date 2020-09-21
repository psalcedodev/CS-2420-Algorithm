import random


def createRandomList(size):
    A = []
    for i in range(size):
        A.append(i)
    for i in range(size):
        r = random.randrange(0, size)
        A[i], A[r] = A[r], A[i]
    return A
