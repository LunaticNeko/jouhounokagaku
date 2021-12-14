import matplotlib.pyplot as plt
import numpy as np

x0 = np.array(range(5))
x1 = np.array(range(10))
x2 = np.array(range(100))

fig, axs = plt.subplots(1,3)
fig.suptitle("Comparison of Time Complexity Levels")

for ax in axs.flat:
    ax.set(xlabel="Input value n", ylabel="Maximum number of calculations")
for ax in axs.flat:
    ax.label_outer()

axs[0].plot(x0,x0, label="O(n)")
axs[0].plot(x0,x0/2, label="O(n/2)")
axs[0].plot(x0,np.sqrt(x0), label="O(sqrt(n))")
axs[0].plot(x0,np.power(x0,2), label="O(n^2)")

axs[1].plot(x1,x1, label="O(n)")
axs[1].plot(x1,x1/2, label="O(n/2)")
axs[1].plot(x1,np.sqrt(x1), label="O(sqrt(n))")
axs[1].plot(x1,np.power(x1,2), label="O(n^2)")

axs[2].plot(x2,x2, label="O(n)")
axs[2].plot(x2,x2/2, label="O(n/2)")
axs[2].plot(x2,np.sqrt(x2), label="O(sqrt(n))")
axs[2].plot(x2,np.power(x2,2), label="O(n^2)")

axs[0].legend()
axs[1].legend()
axs[2].legend()

plt.show()

