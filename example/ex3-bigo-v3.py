import matplotlib.pyplot as plt
import numpy as np

x0 = np.array(range(1,40))

fig, ax = plt.subplots(1,1)
fig.suptitle("Comparison of Time Complexity Levels")

ax.set(xlabel="Number of objects", ylabel="Number of comparisons")

ax.plot(x0,x0, label="O(n)")
ax.plot(x0,np.power(x0,2), label="O(n^2)")
ax.plot(x0,np.log2(x0)*x0, label="O(n log n)")

ax.legend()

plt.show()

