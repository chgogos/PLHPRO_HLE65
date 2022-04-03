import pandas as pd
import matplotlib.pyplot as plt
dataset_url = 'http://www.ceti.gr/chairiq/ml_courses/datasets/Fuel_Consumption.csv'
data0 = pd.read_csv(dataset_url) # Φωρτόνουμε τα δεδομένα

data = data0[["ENGINESIZE","CO2EMISSIONS"]] # Επιλέγουμε μόνο 2 στήλες
print(data.head()) # Προβάλουμε τις πρώτες 5 εγγραφές
print(data.info()) # Προβάλουμε πληροφορίες για το σύνολο δεδομένων

# Δημιουργία γραφήματος
plt.scatter(data["ENGINESIZE"],data["CO2EMISSIONS"])
plt.title("ENGINESIZE VS CO2EMISSIONS")
plt.xlabel("Enginesize")
plt.ylabel("Emission")
plt.show()
