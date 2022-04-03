import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = datasets.load_iris()
p_length = iris.data[:,2]
p_width = iris.data[:,3]

x_train = np.array([p_length,p_width]).T

kmeans = KMeans(n_clusters=3) # Αρχικοποίηση μοντέλου KMeans με 3 ομάδες
y_pred = kmeans.fit(x_train) #Εκπαίδευση μοντέλου

print(kmeans.labels_) # Ομάδες δεδομένων
print(kmeans.cluster_centers_) # Κενtρικά σημεία κάθε ομάδας

plt.scatter(x_train[:,0],x_train[:,1], c=kmeans.labels_ ,cmap='rainbow') # Δεδομένα χρωματισμένα ανάλογα την ομάδα στους
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], s=500, marker= "*", color='black', edgecolor='white') # Κεντρικά σημεία κάθε ομάδας
plt.title("Petal Length - Width")
plt.xlabel('Length')
plt.ylabel("Width")
plt.show()