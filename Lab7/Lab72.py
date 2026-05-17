n = int(input("Ingrese un número par: "))

if n % 2 != 0:
    print("El número debe ser par.")
else:
    for i in range(n):
        for j in range(n):
            if i == j:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()
