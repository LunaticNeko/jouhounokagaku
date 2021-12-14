# Implementation of Knapsack Problem Solving in Greedy Algorithm
# Chawanat Nakasan, Kanazawa University, MIT License.

# Set the following variable to True if you want to see step-by-step explanation
verbose_greedy = False
verbose_genetic = False

import random

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
# Greedy will produce [11] which is not globally optimal.

def knapsack_greedy(MW, IL):
    vwratios = []
    for index, item in enumerate(IL):
        vwratios.append(((float(item[1])/item[0]), item[0], item[1], index))
    vwratios = sorted(vwratios, reverse=True)

    if verbose_greedy:
        print("Greedy: Item list sorted by V/W ratio")
        for item in vwratios:
            print(item)

    knapsack_content = []
    TW = 0
    TV = 0

    if verbose_greedy:
        print()

    for candidate_item in vwratios:
        if TW+candidate_item[1] <= MW:
            if verbose_greedy:
                print("Item Added:", candidate_item)
            TW += candidate_item[1]
            TV += candidate_item[2]
            knapsack_content.append(candidate_item[3])
    return (TV, TW, knapsack_content)

print(knapsack_greedy(MW, IL))
