# Leer líneas específicas del archivo
with open("archivo_demo.txt") as f:
    print(f.readline())
    print(f.readline())

# Recorrer todo el archivo línea por línea
with open("archivo_demo.txt") as f:
    for x in f:
        print(x)
``