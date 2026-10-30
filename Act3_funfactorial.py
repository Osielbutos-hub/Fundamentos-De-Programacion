def factorizar(numero):
    print("Los factores de", numero, "son:")

    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)


numero = int(input("Ingresa un número: "))

factorizar(numero)