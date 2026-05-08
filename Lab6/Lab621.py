miTupla = ("asignacion", "laboratorio", "funcion", "parametros", "python")
myit = iter(miTupla)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "casa"
myit2 = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))


for x in mystr:
    print(x)
    