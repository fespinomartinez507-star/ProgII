import string

def contar_palabras_unicas(texto):
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    palabras = texto.split()
    return len(set(palabras))


def palabra_mas_larga(texto):
    palabras = texto.split()
    return max(palabras, key=len)


def frecuencia_caracteres(texto):
    texto = texto.replace(" ", "").lower()
    total = len(texto)
    
    frecuencia = {}
    
    for letra in texto:
        frecuencia[letra] = frecuencia.get(letra, 0) + 1
    
    for letra, conteo in frecuencia.items():
        porcentaje = (conteo / total) * 100
        print(f"{letra}: {porcentaje:.2f}%")


# Flujo principal
texto = input("Ingrese un texto: ")

print("\n--- RESULTADOS ---")
print("Palabras únicas:", contar_palabras_unicas(texto))
print("Palabra más larga:", palabra_mas_larga(texto))
print("Frecuencia de caracteres:")
frecuencia_caracteres(texto)
