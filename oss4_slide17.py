fa = open("countriesΑ.txt", "w")
fa.write("Greece:Athens\nGermany:Berlin\nItaly:Rome")
fa.close()
fb = open("countriesΒ.txt", "w")
fb.write("France:Paris\nGermany:Berlin\nItaly:Amsterdam")
fb.close()

def readFiles(fileA, fileB):
  fa = open(fileA , "r")
  fb = open(fileB , "r")

  txtA = fa.read()
  txtB = fb.read()
  dictionaryA = {}
  dictionaryB = {}

  for line in txtA.split('\n'):
    c = line.split(':')
    dictionaryA[c[0]] = c[1]

  for line in txtB.split('\n'):
    c = line.split(':')
    dictionaryB[c[0]] = c[1]    

  return dictionaryA, dictionaryB

def compDicts(first_dict, second_dict):
  value = {}
  for item in second_dict.items():
    if item[0] not in first_dict.keys():
      value[item] = 'Does not exist in the countriesA.txt file.'
    else:
       if item[1] != first_dict[item[0]]:
          value[item] = 'Wrong capital. The correct is:', first_dict[item[0]]
  return value


dictA, dictB = readFiles('countriesΑ.txt', 'countriesΒ.txt')
res = compDicts(dictA, dictB)
print(res)