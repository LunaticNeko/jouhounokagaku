# Implementation of Knapsack Problem Solving by Genetic Algorithm
# Chawanat Nakasan, Kanazawa University, MIT License.

# Set the following variable to True if you want to see step-by-step explanation
verbose_greedy = False
verbose_genetic = False

import random
import matplotlib.pyplot as plt

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

def random01s(length):
    return [random.randint(0,1) for n in range(length)]

def dotproduct(A, B):
    return sum([A[i]*B[i] for i in range(len(A))])

def random_list_op(candidate, op=0):
    # op == 0 => remove
    # op == 1 => add

    assert (op in [0,1]), "op must be 0 or 1"

    if op == 0:
        if not any(candidate):
            return candidate
    else:
        if all(candidate):
            return candidate

    while True:
        tryindex = random.randint(0, len(candidate)-1)
        if candidate[tryindex] == op:
            continue
        else:
            candidate[tryindex] ^= 1 #flip
            break

    return candidate

# Aliases for knapsack_ga_random_op for readability
def random_add(candidate):
    return random_list_op(candidate, 1)

def random_remove(candidate):
    return random_list_op(candidate, 0)

def random_mutate(candidate):
    return random_list_op(candidate, random.randint(0,1))

# Randomly remove items from candidate until it satisfies weight limit
def ga_filter(candidate, W, MW):
    while dotproduct(candidate, W) > MW:
        candidate = random_remove(candidate)
    return candidate

#
# Parent 1: [************]
# Parent 2: [%%%%%%%%%%%%]
# Child 1:  [******%%%%%%]
# Child 2:  [%%%%%%******]
#
def crossover1(parent1, parent2):
    cp = crossover_point = len(parent1)//2
    return [parent1[:cp] + parent2[cp:], parent2[:cp] + parent1[cp:]]

#
# Parent 1: [************]
# Parent 2: [%%%%%%%%%%%%]
# Child 1:  [*%*%*%*%*%*%]
# Child 2:  [%*%*%*%*%*%*]
#
def crossover2(parent1, parent2):
    c1 = [(parent1[i] if i%2 else parent2[i]) for i in range(len(parent1))]
    c2 = [(parent2[i] if i%2 else parent1[i]) for i in range(len(parent1))]
    return [c1, c2]

def knapsack_ga_board_value(candidates):
    return sum([dotproduct(candidate, V) for candidate in candidates])

log_x = []
log_y = []

# Solve Knapsack using GA. nc is size of candidate pool.
def knapsack_ga(MW, W, V, genlimit=100, nc=60, log=False):
    global log_x
    global log_y
    if nc % 1 != 0:
        nc += 1 #ensure that nc is always even

    candidates = [ga_filter(random01s(len(W)), W, MW) for n in range(nc)]

    maxv = 0
    optc = ()

    total_generations = 0

    if verbose_genetic:
        print("\n\nKNAPSACK ALGORITHM\nInitial candidates (0 = item not in knapsack, 1 = in):")
        for candidate in candidates:
            print(candidate, dotproduct(candidate, V))

    while total_generations <= genlimit:
        total_generations += 1

        new_candidates = []

        # Select
        selection_list = sorted([(dotproduct(candidate, V), candidate) for candidate in candidates], reverse=True)[:nc//2]
        candidates = [candidate for (value, candidate) in selection_list]

        # Crossover
        for i in range(0, nc//2, 2):
            new_candidates += crossover1(candidates[i], candidates[i+1])
            new_candidates += crossover2(candidates[i], candidates[i+1])
        candidates = new_candidates

        # Mutate (and filter to ensure criteria rules)
        candidates = [ga_filter(random_mutate(candidate), W, MW) for candidate in candidates]

        # Seek the best candidate, save
        bestcandidate = sorted([(dotproduct(candidate, V), dotproduct(candidate, W), candidate) for candidate in candidates], reverse=True)[0]
        if bestcandidate[0] > maxv:
            maxv = bestcandidate[0]
            optc = bestcandidate

        if log:
            log_x.append(total_generations)
            log_y.append(maxv)

    return optc

def demo():
    print("Knapsack content produced by Genetic Alg. (60 candidates):")
    print("I'll run this many times and show only the best total values.")
    for i in range(20):
        results = [knapsack_ga(MW, W, V, i, nc=60)[0] for j in range(10)]
        print("{:>5} generations:".format(i), results)

def demo_chartperf():
    print("Running demo simulation with performance chart:")
    for i in range(100):
        knapsack_ga(MW, W, V, 100, nc=4, log=True)
    fig, ax = plt.subplots(figsize=(2,3))
    ax.scatter(log_x, log_y, s=8)
    ax.set_title("Highest value obtained by genetic algorithm")
    ax.set_xlabel("Generations")
    ax.set_ylabel("Maximum Solution Value")
    plt.show()

