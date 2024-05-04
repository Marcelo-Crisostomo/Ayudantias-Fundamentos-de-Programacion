#1 - Entrada / 2 - Proceso / 3 - Salida 
#Que datos necesito para calcular el IMC - Formula Peso y Altura
#1-Solicicitar los datos al usuario - Input - Float
peso = float(input("Ingresa tu peso en kilos: formato 50 "))
#solicitar la altura al usuario
altura = float(input("Ingresa tu altura formato: 1.65 "))
# Hacer el proceso calcular el IMC p/(a*2)
imc = peso / (altura*2)

#Imprimir el resultado del imc con dos decimales
#{valor:.Nf}
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f} ")