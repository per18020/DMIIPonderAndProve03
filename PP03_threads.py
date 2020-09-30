from math import sqrt, floor, sin, pi, ceil
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

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

def worker(iterator):
    for number in iterator:
        if (not ABUnion(number) and ABIntersection(number)): return False
    return True

def startWorkers(offset):
    ranges = []
    for i in range(WORKERS):
        ranges.append(range(BLOCKSIZE * (i - 1 + offset), BLOCKSIZE * (i + offset)))
    with ThreadPoolExecutor(max_workers=WORKERS) as excecutor:
        future_to_result = {excecutor.submit(worker, r): r for r in ranges}
        for future in as_completed(future_to_result):
            if not future.result(): return False
    return True

iterations = 0
while True:
    time_start = time.perf_counter()
    startWorkers(iterations)
    iterations += 1
    time_elapsed = (time.perf_counter() - time_start)
    # print ("%5.10f microseconds per iteration" % ((time_elapsed / (iterations * WORKERS * BLOCKSIZE)) * 1000000))
    print ("%5.10f seconds for %.0f iterations" % (time_elapsed, WORKERS * BLOCKSIZE))
    