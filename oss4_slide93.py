from sklearn import datasets

iris = datasets.load_iris()
print(iris.data) # Εκτύπωση όλων των δεδομένων εισόδου
print(type(iris.data))
print(iris.target) # Εκτύπωση όλων των δεδομένων εξόδου
print(type(iris.target))
print(iris.target_names) # Εκτύπωση των ονομάτων των τριών κλάσεων

print(iris.data[15], '(',iris.target[15], ')', iris.target_names[iris.target[15]]) # Εκτύπωση ενός δείγματος

print('Size, X:', iris.data.size,', Y:',iris.target.size)  # Εκτύπωση μεγέθους συνόλου δεδομένων
print('Shape, X', iris.data.shape,', Y:',iris.target.shape)  # Εκτύπωση διαστάσεων συνόλου δεδομένων