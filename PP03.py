from numba import jit
from math import sqrt, sin, pi
from datetime import datetime
import requests
import time

BASEURL = "https://discrete-math-2-ponder-prove-3.herokuapp.com"
# BASEURL = "http://localhost:5000"

def getValidatedInt(msg, validationFunction):
    while True:
        try:
            userInput = int(input(msg))
        except:
            continue
        if validationFunction(userInput):
            return userInput
        
def next():
    response = requests.get(BASEURL + "/api/next").json()
    return response['next']

def getConfig():
    return requests.get(BASEURL + "/api/config").json()
    
def shouldWait():
    response = requests.get(BASEURL + "/api/shouldWait").json()
    return response['wait']

def shouldContinue():
    response = requests.get(BASEURL + "/api/shouldContinue").json()
    return response['continue']

def sendStatus(data):
    requests.post(BASEURL + "/api/status", { "testCount":data[0], "didSucceed":data[1] })

print("Getting configuration from the server...")

PISQR2 = pi / sqrt(2)
BLOCKSIZE = getConfig()['blockSize']

@jit
def run(iteration):
    for index in range(iteration * BLOCKSIZE, (iteration + 1) * BLOCKSIZE):
        lhs = sin(index * PISQR2) * sin((index + 1) * PISQR2)
        if (not ((lhs <= 0) ^ (lhs > 0))):
            return (index, False)
    return (index, True)

while shouldWait():
    print("Waiting to start... checking again in 30 seconds")
    time.sleep(30)

print("Started at " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
while shouldContinue():
    output = run(next())
    sendStatus(output)
    print(str(output) + " " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
print("Stopped at " + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))