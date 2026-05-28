# Crear el archivo y escribir contenido
with open("archivo_demo.txt", "w") as f:
    f.write("¡Hola! Bienvenido a archivo_demo.txt\n")
    f.write("Este archivo es para fines de prueba.\n")
    f.write("¡Buena suerte!\n")

# Leer todo el archivo
with open("archivo_demo.txt", "r") as f:
    print(f.read())

# Leer solo una línea
f = open("archivo_demo.txt")
print(f.readline())
f.close()
