# Για την δημιουργία του αρχείου
f = open('myfile.txt','w')
l1 = "Hello World!.\n"
f.write(l1)
f.close()

f = open("myfile.txt", "r")
txt = f.read()

print(type(txt))
print(txt)