# Solicitar al usuario ingresar el tipo de proyecto y el lenguaje
proyecto = input("Ingresa el tipo de proyecto (pequeño, mediano o grande): ").lower()
lenguaje = input("Ingresa el lenguaje de programación: ").lower()

# Estructura if-elif-else anidada para estimar el tiempo de desarrollo
if proyecto == "pequeño":
    if lenguaje == "python":
        print("El tiempo estimado de desarrollo es de 2 semanas.")
    else:
        print("El tiempo estimado de desarrollo es de 3 semanas.")
elif proyecto == "mediano":
    if lenguaje == "python":
        print("El tiempo estimado de desarrollo es de 4 semanas.")
    else:
        print("El tiempo estimado de desarrollo es de 6 semanas.")
elif proyecto == "grande":
    if lenguaje == "python":
        print("El tiempo estimado de desarrollo es de 8 semanas.")
    else:
        print("El tiempo estimado de desarrollo es de 12 semanas.")
else:
    print("Tipo de proyecto no válido.")