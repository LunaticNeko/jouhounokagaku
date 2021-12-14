# Linear Regression Example
# Chawanat Nakasan, Kanazawa University, MIT License.

# Config lines

savefigs = True # Save all figures (file names are set in figfilename)
showfigs = True # Show all figures
tutmsgs = True  # Show tutorial messages
verbose = True  # Show verbose regression process

# Leave the first element blank so we can start from [1]. Much better
# semantically.
figfilename = ['','ex4-ml-fig1.png','ex4-ml-fig2.png','ex4-ml-fig3.png','ex4-ml-fig4.png','ex4-ml-fig5.png']

#

import csv
import math

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    sys.exit("""This program requires matplotlib and numpy.
                Type \"pip install matplotlib numpy\" in your terminal,
                complete installation process, and try again."""


headers = []
index = {}
data = []

def cost(x, y, m, c):
    yp = [(m*xi + c) for xi in x]
    return sum([(y[i]-yp[i])**2 for i in range(len(y))])/2

#returns nth column of an array
def col(arr, n):
    return [item[n] for item in arr]


#
# SECTION 1: Data Import and Visualization
# This will import data from the specified file and display a univariate
# data with size in sqm as independent variable (X) and total cost per month as
# dependent variable (Y).
#

with open('ex4-ml-apartments.csv', 'r', encoding='utf-8-sig') as f:
    r = csv.reader(f)
    row = next(r)
    headers = row
    for i, h in enumerate(headers):
        index[h] = i
    for row in r:
        data.append(tuple(map(int, row)))

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(col(data, index['sqm']), col(data, index['TotalPrice']), label="data point")
ax.set_title("Rent of Properties around Tagami/Morinosato based on Room sqm-size")
ax.set_xlabel("Size (sq.m.)")
ax.set_ylabel("Total Rent (thousand yen)")
ax.set_xlim([0,80])
if savefigs: plt.savefig(figfilename[1])
if showfigs: plt.show()

mrange = np.arange(0,3,.05)
crange = np.arange(-70,70,0.2)
M = []
C = []
Z = []
for m in mrange:
    for c in crange:
        M.append(m)
        C.append(c)
        Z.append(cost(col(data, index['sqm']), col(data, index['TotalPrice']), m, c))

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(M, C, s=4, c=list(map(math.log,Z)), cmap='Blues')
ax.set_title("How close we are to the best regression parameters")
ax.set_xlabel("m (theta1)")
ax.set_ylabel("c (theta0)")
if savefigs: plt.savefig(figfilename[2])
if showfigs: plt.show()

# Now let's get regressing for real


# This is the dotproduct from back in Knapsack ...
def dotproduct(A, B):
    return sum([A[i]*B[i] for i in range(len(A))])


h = dotproduct #for now


def cost_gd(x, y, theta):
    n = len(x[0])
    return sum([(h(theta, col(x,i)) - y[i])**2 for i in range(n)])/2



# Now we'll begin optimizing for real
def gradient_descent(x, y, alpha=0.000001, iter_limit=100):
    # pad x with an additional vector of ones
    n = len(x[0])
    x = [[1]*n] + x
    theta = [0] * (len(x))

    cost_log = []
    theta_log = []

    for iter_count in range(iter_limit):
        #print(iter_count, theta)
        for j in range(len(x)):
            theta[j] += alpha * \
                        sum([(y[i] - h(theta, col(x, i)))*x[j][i] for i in range(n)])
        cost_log.append(cost_gd(x, y, theta))
        theta_log.append([theta[j] for j in range(len(x))])
    return theta, cost_log, theta_log


iters = 80000

result_theta, cost_log, theta_log = gradient_descent([col(data, index['sqm'])], col(data, index['TotalPrice']), alpha=0.000001, iter_limit=iters)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,6), sharey=True)
fig.suptitle("Cost of Gradient Descent (Housing Dataset)")
ax1.plot(list(range(iters)), cost_log)
ax1.set_xlabel("Generations")
ax1.set_ylabel("Cost")
ax2.plot(list(range(iters)), cost_log)
ax2.set_xlabel("Generations")
ax2.set_xlim([0,200])
if savefigs: plt.savefig(figfilename[3])
if showfigs: plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,6))
fig.suptitle("Movement of m and c (theta1 and theta0) over iterations")
ax1.scatter(M, C, s=4, c=list(map(math.log,Z)), cmap='Blues')
ax1.scatter(col(theta_log, 0), col(theta_log, 1), s=4, color="red")
ax2.set_xlim([0,2])
ax2.set_ylim([-20,20])
ax1.set_xlabel("m (theta1)")
ax1.set_ylabel("c (theta0)")
ax2.scatter(M, C, s=4, c=list(map(math.log,Z)), cmap='Blues')
ax2.scatter(col(theta_log, 0), col(theta_log, 1), s=4, color="red")
ax2.set_xlim([0,1.5])
ax2.set_ylim([-2,2])
ax2.set_xlabel("m (theta1)")
if savefigs: plt.savefig(figfilename[4])
if showfigs: plt.show()

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(col(data, index['sqm']), col(data, index['TotalPrice']), label="data point")
ax.plot(list(range(0,80)),\
        [result_theta[1]*x + result_theta[0] for x in range(0,80)], color="red", label="y = {:.4f}x+{:.4f}".format(result_theta[1],result_theta[0]))
ax.set_title("Rent of Properties around Tagami/Morinosato based on Room sqm-size")
ax.set_xlabel("Size (sq.m.)")
ax.set_ylabel("Total Rent (thousand yen)")
ax.set_xlim([0,80])
ax.legend()
if savefigs: plt.savefig(figfilename[5])
if showfigs: plt.show()

