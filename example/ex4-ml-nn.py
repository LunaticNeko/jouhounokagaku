# Two-Node (1 Hidden, 1 Output) Neural Network Example
# Chawanat Nakasan, Kanazawa University, MIT License.

import csv
import matplotlib.pyplot as plt
import math
import numpy as np
import random


headers = []
index = {}
data = []

def cost(x, y, m, c):
    yp = [(m*xi + c) for xi in x]
    return sum([(y[i]-yp[i])**2 for i in range(len(y))])/2

#returns nth column of an array
def col(arr, n):
    return [item[n] for item in arr]


#MAIN

with open('ex4-ml-apartments.csv', 'r', encoding='utf-8-sig') as f:
    r = csv.reader(f)
    row = next(r)
    headers = row
    for i, h in enumerate(headers):
        index[h] = i
    for row in r:
        data.append(tuple(map(int, row)))

def dotproduct(A, B):
    return sum([A[i]*B[i] for i in range(len(A))])

def neuron_act(weights, inputs):
    return dotproduct(weights, inputs+[1])

def s(x):
    return 1/(1+math.e**(-x))

def nn(x):
    iterlimit = 100
    # create the network
    inputs = 4
    hidden_nodes = 1
    output_nodes = 1

    input_weights = [random.random() for i in range(inputs+1)]
    hidden_weights = [random.random() for i in range(hidden_nodes+1)]
    output_weights = [random.random() for i in range(output_nodes+1)]

    #fwd prop
    hidden_value =


    for iters in range(iterlimit):

