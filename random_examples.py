import random

# random.seed(35)

print(random.random())  # επιστροφή πραγματικής τιμής μεταξύ 0 και 1
print(random.randint(1, 10))  # επιλογή μιας τιμής από τις 0,2,4,6,8,10
print(random.randrange(0, 10, 2))  # επιλογή μιας τιμής από τις 0,2,4,6,8,10
print(random.uniform(1, 10))  # επιλογή πραγματικής τιμής στο διάστημα [1,10]
print(random.choice(["a", "b", "c", "d"]))  # επιλογή 1 τιμής από τη λίστα
print(random.choices(["a", "b", "c", "d"], k=4))  # επιλογή 4 τιμών με πιθανά διπλότυπα
print(random.sample(["a", "b", "c", "d", "e"], k=4))  ## επιλογή 4 τιμών χωρίς διπλότυπα
