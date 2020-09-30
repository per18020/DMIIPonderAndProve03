from math import sqrt, floor, sin, pi, ceil

SQR2 = sqrt(2)

def computeFinite(testFunction, iterator):
    out = set()
    for number in iterator:
        if testFunction(number):
            out.add(number)
    return out


def union(testFunctionOne, testFunctionTwo):
    return lambda target: testFunctionOne(target) or testFunctionTwo(target)


def intersection(testFunctionOne, testFunctionTwo):
    return lambda target: testFunctionOne(target) and testFunctionTwo(target)


def complement(testFunction):
    return lambda target: not testFunction(target)


def testA(target):
    return sin(target * pi / SQR2) * sin((target + 1) * pi / SQR2) <= 0

def testB(target):
    return sin(target * pi / SQR2) * sin((target + 1) * pi / SQR2) >= 0

print(
    computeFinite(testA, range(0, 100))
)

print(
    computeFinite(testB, range(0, 100))
)


ABUnion = union(testA, testB)

def doWork(iterator):
    for number in iterator:
        print(number)
        if (not ABUnion(number)): return False
    return True


blockSize = 10000

iterations = 1
while True:
    print(doWork(range(blockSize * (iterations - 1), blockSize * iterations)))
    iterations += 1