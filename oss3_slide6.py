def add(x,y):
    res = x + y 
    return res 

c = add(10, 20)
print ('1η Πρόσθεση: ', c)

e = add(c, 15)
print ('2η Πρόσθεση: ', e)

def car(id, st, clr):
  res = str(id) +' '+ st +' '+ clr
  return res

print(car(1, 'Οικογενειακό','Πράσινο'))
print(car(2, 'Σπορ','Κόκκινο'))
print(car(3, 'Νεανικό','Μπλε'))