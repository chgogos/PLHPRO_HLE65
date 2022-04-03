f = open("myfile.txt", "a")
f.write("\nNew line")
f.close()

f = open("myfile.txt", "r")
print(f.read())

f = open("myfile.txt", "w")
print(f.write("New Text!"))
f.close()

f = open("myfile.txt", "r")
print(f.read())