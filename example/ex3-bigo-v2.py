import matplotlib.pyplot as plt
import numpy as np

x0 = np.array(range(10))
x1 = np.array(range(30))

fig, axs = plt.subplots(1,2)
fig.suptitle("Comparison of Time Complexity Levels")

for ax in axs.flat:
    ax.set(xlabel="Number of objects", ylabel="Number of test attempts")
for ax in axs.flat:
    ax.label_outer()

axs[0].plot(x0,x0, label="O(n)")
axs[0].plot(x0,np.power(x0,2), label="O(n^2)")
axs[0].plot(x0,np.power(2,x0), label="O(2^n)")

axs[1].plot(x1,x1, label="O(n)")
axs[1].plot(x1,np.power(x1,2), label="O(n^2)")
axs[1].plot(x1,np.power(2,x1), label="O(2^n)")

axs[0].legend()
axs[1].legend()

plt.show()

