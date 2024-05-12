# Actividad de Reforzamiento: Liquidación de Sueldo con AFP y FONASA

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

# Paso 3: Calcular el descuento de AFP (10%)
descuento_afp = sueldo_bruto * 0.1

# Paso 4: Calcular el descuento de FONASA (7%)
descuento_fonasa = sueldo_bruto * 0.07

# Paso 5: Calcular el total de descuentos
total_descuentos = descuento_afp + descuento_fonasa

# Paso 6: Calcular el sueldo líquido
sueldo_liquido = sueldo_bruto - total_descuentos

# Paso 7: Mostrar el desglose de los cálculos en pantalla
print("Liquidación de Sueldo")
print("---------------------")
print(f"Sueldo Bruto: ${sueldo_bruto:,.0f}")
print(f"Descuento AFP (10%): ${descuento_afp:,.0f}")
print(f"Descuento FONASA (7%): ${descuento_fonasa:,.0f}")
print(f"Total Descuentos: ${total_descuentos:,.0f}")
print(f"Sueldo Líquido: ${sueldo_liquido:,.0f}")

# Paso 8: Escribir los datos en un archivo de texto con el nombre del usuario
nombre_archivo = f"{nombre_usuario}.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write("Liquidación de Sueldo\n")
    archivo.write("---------------------\n")
    archivo.write(f"Sueldo Bruto: ${sueldo_bruto:,.0f}\n")
    archivo.write(f"Descuento AFP (10%): ${descuento_afp:,.0f}\n")
    archivo.write(f"Descuento FONASA (7%): ${descuento_fonasa:,.0f}\n")
    archivo.write(f"Total Descuentos: ${total_descuentos:,.0f}\n")
    archivo.write(f"Sueldo Líquido: ${sueldo_liquido:,.0f}\n")

print(f"Los datos se han guardado en el archivo {nombre_archivo}.")