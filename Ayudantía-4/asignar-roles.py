# Solicitar al usuario ingresar la cantidad de años de experiencia
experiencia = float(input("Ingresa tus años de experiencia en programación: "))

# Asignar el rol según la experiencia utilizando if-elif-else
if experiencia < 2:
    rol = "Desarrollador Junior"
elif experiencia <= 5:
    rol = "Desarrollador Senior"
else:
    rol = "Líder de Equipo"

# Imprimir el rol asignado
print(f"Tu rol en el equipo de desarrollo es: {rol}")