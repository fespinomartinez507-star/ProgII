# Pedir número al usuario
n = int(input("Ingrese un número: "))

factorial = 1

# Calcular factorial
if n < 0:
    print("El factorial no existe para números negativos")
else:
    for i in range(1, n + 1):
        factorial *= i

    print(f"El factorial de {n} es: {factorial}")
