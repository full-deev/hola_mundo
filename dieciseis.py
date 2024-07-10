#Muestro un titulo bonito
print("Calculadora de IMC")
#pido al usuario que ingrese el peso y la altura
peso = float(input("Ingrese el peso en -KG- "))
alt = float(input("Ingresa la altura en -cm- "))
#convierto la altura a metros
alt = alt / 100
#calculo el imc
imc = peso / (alt ** 2)
#redondeo el resultado a solo 2 decimales
imc = round(imc, 2)
#mediante un print - muestro el resultado segun diferentes categorias que consulte previamente
if imc < 18.5:
  print(f"Su IMC es {imc} y está considerado con bajo peso")
elif imc >= 18.5 and imc <= 24.9:
  print(f"Su IMC es {imc} y se considerado con un peso adecuado")
elif imc >= 25.0 and imc <= 29.9:
  print(f"Su IMC es {imc} y está considerado con Sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
  print(f"Su IMC es {imc} y está considerado con Obesidad I")
elif imc >= 35.0 and imc <= 39.9:
  print(f"Su IMC es {imc} y está considerado con Obesidad II")
elif imc >= 40:
  print(f"Su IMC es {imc} y está considerado con Obesidad Grave")