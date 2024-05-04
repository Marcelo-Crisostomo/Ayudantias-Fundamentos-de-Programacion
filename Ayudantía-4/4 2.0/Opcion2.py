def calcular_bonificacion(antiguedad, desempeno):
    """
    Calcula la bonificación correspondiente según la antigüedad y el desempeño del empleado.
    
    Args:
        antiguedad (int): Antigüedad del empleado en años.
        desempeno (str): Evaluación de desempeño del empleado ('A', 'B' o 'C').
        
    Returns:
        float: Porcentaje de bonificación.
    """
    if antiguedad < 2:
        if desempeno == 'A':
            return 0.05
        elif desempeno == 'B':
            return 0.03
        else:
            return 0
    elif antiguedad <= 5:
        if desempeno == 'A':
            return 0.08
        elif desempeno == 'B':
            return 0.05
        else:
            return 0.02
    else:
        if desempeno == 'A':
            return 0.12
        elif desempeno == 'B':
            return 0.08
        else:
            return 0.05

# Solicitar información del empleado
nombre = input("Ingrese el nombre del empleado: ")
antiguedad = int(input("Ingrese la antigüedad del empleado (en años): "))
desempeno = input("Ingrese la evaluación de desempeño del empleado (A, B o C): ")

# Calcular bonificación y sueldo total
sueldo_base = 1000000
bonificacion_porcentaje = calcular_bonificacion(antiguedad, desempeno)
bonificacion = sueldo_base * bonificacion_porcentaje
sueldo_total = sueldo_base + bonificacion

# Mostrar resultados
print(f"\nBonificación para el empleado {nombre}:")
print(f"Sueldo base: ${sueldo_base:,.0f}")
print(f"Bonificación ({bonificacion_porcentaje*100:.0f}%): ${bonificacion:,.0f}")
print(f"Sueldo total: ${sueldo_total:,.0f}")