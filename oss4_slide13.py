# Για την δημιουργία του αρχείου
f = open("countries.txt", "w")
f.write("Greece : Athens\nGermany : Berlin\nItaly : Rome")
f.close()

f = open("countries.txt", "r")
txt = f.read()
dictionary = {}
for line in txt.split('\n'):
    c = line.split(':')
    dictionary[c[0]] = c[1]
f.close()

print(dictionary)

f = open("countries.txt", "r")
dictionary2 = {}
txt = f.readlines()
for line in txt:
    c = line.split(':')
    dictionary2[c[0]] = c[1]
f.close()

print(dictionary2)