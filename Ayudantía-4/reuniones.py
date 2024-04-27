# Solicitar al usuario ingresar el día de la semana
dia = input("Ingresa el día de la semana (lunes, martes, miércoles, etc.): ").lower()

# Estructura if-elif-else para determinar si se debe organizar una reunión
if dia == "lunes" or dia == "jueves":
    print("Hoy es día de reunión de equipo.")
elif dia == "viernes":
    print("Hoy no hay reunión, pero es un buen día para revisar el progreso de la semana.")
else:
    print("Hoy no hay reunión programada.")