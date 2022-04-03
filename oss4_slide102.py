from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
p_length = iris.data[:,2]
p_width = iris.data[:,3]

x_train = np.array([p_length,p_width]).T
print(x_train[:5])

plt.scatter(p_length,p_width)
plt.title("Petal Length - Width")
plt.xlabel('Length')
plt.ylabel("Width")
plt.show()