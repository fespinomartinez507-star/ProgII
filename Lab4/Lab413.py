datos = bytearray(b"Hola Mundo")
vista = memoryview(datos)
vista[0] = 104 # Cambia 'H' a 'h' (ASCII 104)
print(datos)
