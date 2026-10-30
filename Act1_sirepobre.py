calificacion = float(input("Ingresa tu calificación: "))

if calificacion < 0 or calificacion > 100:
    print("Error: La calificación debe estar entre 0 y 100")

elif calificacion >= 70:
    print("¡Felicidades, aprobaste!")

else:
    print("Reprobaste la materia.")
