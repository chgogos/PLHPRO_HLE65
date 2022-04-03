import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

print('------------------Προετοιμασία δεδομένων--------------------------------')
dataset_url = 'http://www.ceti.gr/chairiq/ml_courses/datasets/Fuel_Consumption.csv'
data = pd.read_csv(dataset_url)
data = data[["ENGINESIZE","CO2EMISSIONS"]]

num = int(len(data)*0.8) # Ψάχνουμε για τον αριθμό των 80% των εγγραφών 
train = data[:num] # 80% Δεδομένα εκπαίδευσης
test = data[num:]# 20% Δεδομένα δοκιμών
print ("Data:",len(data),", Train:",len(train),", Test:",len(test))

x_train = np.array(train[["ENGINESIZE"]])  # Δεδομένα εισόδου εκπαίδευση
y_train = np.array(train[["CO2EMISSIONS"]])# Δεδομένα εξόδου εκπαίδευση
x_test = np.array(test[["ENGINESIZE"]])    # Δεδομένα εισόδου δοκιμών
y_test = np.array(test[["CO2EMISSIONS"]])  # Δεδομένα εξόδου δοκιμών

print('------------------Εκπαίδευση και αξιολόγηση επίδοσης----------------------')
regr = linear_model.LinearRegression() # Επιλογή μοντέλου γραμμικής παλυνδρόμησης
regr.fit(x_train,y_train) #Εκπαίδευση μοντέλου

coefficients = regr.coef_
intercept = regr.intercept_

y_pred = regr.predict(x_test) #Δοκιμή μοντέλου στο x_test
print("Coefficients: \n", coefficients)# The coefficients
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))# Μέσο τετραγωνικό σφάλμα, όσο μικρότερο τόσο καλύτερο, 0 έχουμε την τέλεια πρόβλεψη
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred)) # Εαν η τιμή είναι 1 τότε έχουμε την τέλεια πρόβλεψη

print('-------------------Δοκιμή σε νέα δεδομένα--------------------------------')
x_test2 = np.array([[2.1],[1.2],[3.3]])
y_pred2 = regr.predict(x_test2)
print(y_pred2)

print('-----------------Προβολή μοντέλου στα  δεδομέν εκπαίδευσης--------------------------------')
print ("Slope: ",coefficients[0],"Intercept: ",intercept) # Slope  and Intercept:         

plt.scatter(train["ENGINESIZE"], train["CO2EMISSIONS"])
plt.plot(x_train, coefficients[0]*x_train + intercept,color="red")
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()