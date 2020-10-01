from numba import jit
from math import sqrt, sin, pi
from datetime import datetime

SQR2 = sqrt(2)
BLOCKSIZE = 100000000

def getValidatedInt(msg, validationFunction):
    while True:
        try:
            userInput = int(input(msg))
        except:
            continue
        if validationFunction(userInput):
            return userInput

@jit
def run(iteration):
    for index in range(iteration * BLOCKSIZE, (iteration + 1) * BLOCKSIZE):
        if (not ((sin(index * pi / SQR2) * sin((index + 1) * pi / SQR2) <= 0) or (sin(index * pi / SQR2) * sin((index + 1) * pi / SQR2) >= 0))):
            return (index, False)
    return (index, True)

clusterSize = getValidatedInt("Enter cluster size: ", lambda clusterSize: not (clusterSize < 0))
clusterIndex = getValidatedInt("Enter cluster index: ", lambda clusterIndex: not (clusterIndex > clusterSize - 1 or clusterIndex < 0))

print("Started at " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
iteration = 0
while True:
    output = run(clusterIndex + (iteration * clusterSize))
    print(str(output) + " " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    iteration += 1