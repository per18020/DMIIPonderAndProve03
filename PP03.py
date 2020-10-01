from numba import jit
from math import sqrt, sin, pi
from datetime import datetime
import requests
import time

print("Getting configuration from the server...")

baseURL = "http://localhost:5000"
config = requests.get(baseURL + "/api/config").json()

SQR2 = sqrt(2)
BLOCKSIZE = config['blockSize']

def getValidatedInt(msg, validationFunction):
    while True:
        try:
            userInput = int(input(msg))
        except:
            continue
        if validationFunction(userInput):
            return userInput
        
def next():
    response = requests.get(baseURL + "/api/next").json()
    return response['next']

def shouldWait():
    response = requests.get(baseURL + "/api/shouldWait").json()
    return response['wait']

def shouldContinue():
    response = requests.get(baseURL + "/api/shouldContinue").json()
    return response['continue']

@jit
def run(iteration):
    for index in range(iteration * BLOCKSIZE, (iteration + 1) * BLOCKSIZE):
        if (not ((sin(index * pi / SQR2) * sin((index + 1) * pi / SQR2) <= 0) or (sin(index * pi / SQR2) * sin((index + 1) * pi / SQR2) >= 0))):
            return (index, False)
    return (index, True)

while shouldWait():
    print("Waiting to start... checking again in 30 seconds")
    time.sleep(30)

print("Started at " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
while shouldContinue():
    output = run(next())
    print(str(output) + " " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))