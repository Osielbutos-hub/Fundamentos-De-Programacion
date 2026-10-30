temperatura = float(input("Ingresa la temperatura del agua: "))

if temperatura <= 0:
    print("El agua está en estado sólido")

elif temperatura < 100:
    print("El agua está en estado líquido")

else:
    print("El agua está en estado gaseoso")

