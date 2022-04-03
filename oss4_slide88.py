import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [2, 4, 6, 8], label="Σειρά-1")
plt.plot([1, 2, 3, 4], [3, 5, 7, 9], label="Σειρά-2")
plt.xlabel("Περιγραφή άξονα x")
plt.ylabel("Περιγραφή άξονα y")
plt.legend(fontsize=8)
plt.show()