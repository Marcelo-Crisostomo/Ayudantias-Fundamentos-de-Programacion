# Actividad de Reforzamiento: Liquidación de Sueldo con AFP, FONASA y Horas Extras
# Paso 1: Solicitar el nombre del usuario
nombre_usuario = input("Ingrese su nombre: ")
# Paso 2: Solicitar el sueldo bruto al usuario
while True:
    try:
        sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
        if sueldo_bruto < 0:
            raise ValueError
        break
    except ValueError:
        print("Error: Ingrese un valor numérico positivo.")
# Paso 3: Solicitar la cantidad de horas extras al usuario
while True:
    try:
        horas_extras = float(input("Ingrese la cantidad de horas extras trabajadas: "))
        if horas_extras < 0:
            raise ValueError
        break
    except ValueError:
        print("Error: Ingrese un valor numérico positivo.")
# Paso 4: Calcular el pago por hora extra (50% adicional)
pago_hora_normal = sueldo_bruto / 180  # Suponiendo 180 horas de trabajo mensuales
pago_hora_extra = pago_hora_normal * 1.5
# Paso 5: Calcular el monto total de horas extras
monto_horas_extras = horas_extras * pago_hora_extra
# Paso 6: Calcular el sueldo bruto total (sueldo base + horas extras)
sueldo_bruto_total = sueldo_bruto + monto_horas_extras
# Paso 7: Calcular el descuento de AFP (10%)
descuento_afp = sueldo_bruto_total * 0.1
# Paso 8: Calcular el descuento de FONASA (7%)
descuento_fonasa = sueldo_bruto_total * 0.07
# Paso 9: Calcular el total de descuentos
total_descuentos = descuento_afp + descuento_fonasa
# Paso 10: Calcular el sueldo líquid
sueldo_liquido = sueldo_bruto_total - total_descuentos
# Paso 11: Mostrar el desglose de los cálculos en pantalla
print("Liquidación de Sueldo")
print("---------------------")
print(f"Sueldo Bruto: ${sueldo_bruto:,.0f}")
print(f"Horas Extras: {horas_extras}")
print(f"Monto Horas Extras: ${monto_horas_extras:,.0f}")
print(f"Sueldo Bruto Total: ${sueldo_bruto_total:,.0f}")
print(f"Descuento AFP (10%): ${descuento_afp:,.0f}")
print(f"Descuento FONASA (7%): ${descuento_fonasa:,.0f}")
print(f"Total Descuentos: ${total_descuentos:,.0f}")
print(f"Sueldo Líquido: ${sueldo_liquido:,.0f}")
# Paso 12: Escribir los datos en un archivo de texto con el nombre del usuario
nombre_archivo = f"{nombre_usuario}.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write("Liquidación de Sueldo\n")
    archivo.write("---------------------\n")
    archivo.write(f"Sueldo Bruto: ${sueldo_bruto:,.0f}\n")
    archivo.write(f"Horas Extras: {horas_extras}\n")
    archivo.write(f"Monto Horas Extras: ${monto_horas_extras:,.0f}\n")
    archivo.write(f"Sueldo Bruto Total: ${sueldo_bruto_total:,.0f}\n")
    archivo.write(f"Descuento AFP (10%): ${descuento_afp:,.0f}\n")
    archivo.write(f"Descuento FONASA (7%): ${descuento_fonasa:,.0f}\n")
    archivo.write(f"Total Descuentos: ${total_descuentos:,.0f}\n")
    archivo.write(f"Sueldo Líquido: ${sueldo_liquido:,.0f}\n")
print(f"Los datos se han guardado en el archivo {nombre_archivo}.")