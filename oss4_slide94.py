import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.10, random_state=42) 

clf = SVC() #Support-Vector Machines Classificator
clf.fit(x_train, y_train) #Εκπαίδευση μοντέλου

y_pred = clf.predict(x_test) #Δοκιμή μοντέλου στο x_test
print(accuracy_score(y_test,y_pred)) #Ακρίβεια εκπαίδευσης

#3 μετρήσεις από λουλούδια
test_data = np.array([[5.1, 3.5, 1.4, 0.2], 
                      [7.0, 3.2, 4.7, 1.4], 
                      [6.3, 3.3, 6.0, 2.5]
                      ])

res = clf.predict(test_data) #Δοκιμή μοντέλου στο 3 μετρήσεις λουλουδιών
for index, x in enumerate(res): #εκτύπωση αποτελεσμάτων
  print(test_data[index], '(', x , ')', iris.target_names[x])
