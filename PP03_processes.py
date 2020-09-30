from math import sqrt, floor, sin, pi, ceil
from multiprocessing import Pool, TimeoutError
import time
import os

def union(testFunctionOne, testFunctionTwo):
    return lambda target: testFunctionOne(target) or testFunctionTwo(target)

def intersection(testFunctionOne, testFunctionTwo):
    return lambda target: testFunctionOne(target) and testFunctionTwo(target)

SQR2 = sqrt(2)
BLOCKSIZE = 10000
WORKERS = 32

def testA(target):
    return sin(target * pi / SQR2) * sin((target + 1) * pi / SQR2) <= 0

def testB(target):
    return sin(target * pi / SQR2) * sin((target + 1) * pi / SQR2) >= 0

ABUnion = union(testA, testB)
ABIntersection = intersection(testA, testB)

# def worker(iterator):
#     for number in iterator:
#         if (not ABUnion(number) and ABIntersection(number)): return False
#     return True

def worker(iterator):
    for number in iterator:
        if (not (sin(number * pi / SQR2) * sin((number + 1) * pi / SQR2) <= 0)):
            return False
    return True

def startProcesses(offset):
        ranges = []
        for i in range(WORKERS):
            ranges.append(range(BLOCKSIZE * (i - 1 + offset), BLOCKSIZE * (i + offset)))
        with Pool(processes=WORKERS) as pool:
            pool.map(worker, ranges, chunksize=100)

if __name__ == '__main__':
    iterations = 0
    while True:
        time_start = time.perf_counter()
        startProcesses(iterations)
        iterations += 1
        time_elapsed = (time.perf_counter() - time_start)
        # print ("%5.10f microseconds per iteration" % ((time_elapsed / (iterations * WORKERS * BLOCKSIZE)) * 1000000))
        print ("%5.10f seconds for %.0f iterations" % (time_elapsed, WORKERS * BLOCKSIZE))
        # print(iterations * WORKERS * BLOCKSIZE)