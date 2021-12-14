# Implementation of Knapsack Problem Solving by Brute-Forcing
# Chawanat Nakasan, Kanazawa University, MIT License.

import random
from itertools import product

MW = max_weight = 200

#IL is encoded by weight then value
IL = item_list = [(15, 12), (90, 15), (20, 120), (120, 720),
                  (25, 30), (40, 240), (20, 120), (50, 20),
                  (30, 20), (20, 18), (35, 55), (191, 1147)]

#W and V split and represented separately
W = []
V = []
for item in IL:
    W.append(item[0])
    V.append(item[1])

# Actually optimal items are: [3, 5, 6, 2]

def dotproduct(A, B):
    return sum([A[i]*B[i] for i in range(len(A))])

def knapsack_bf(MW, W, V):
    max_v = 0
    opt_w = 0
    opt_c = []

    # candidate generation is based on https://stackoverflow.com/questions/25991292
    for candidate in product(range(2), repeat=len(V)):
        this_v = dotproduct(candidate, V)
        this_w = dotproduct(candidate, W)
        print(candidate)
        if this_v >= max_v and this_w <= MW:
            max_v = this_v
            opt_w = this_w
            opt_c = candidate

    return (max_v, opt_w, opt_c)

print(knapsack_bf(MW, W, V))
