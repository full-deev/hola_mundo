#pido al usuario que ingrese un numero
nume = int(input("Ingresa el numero para calcular su factorial: "))
#inicializo la variable fac en 1
fac = 1
#bucle para calcular el factorial
for i in range(1, nume+1):
  #calculo el factorial
  fac *= i
  #muestro el factorial
print(f"El resultado factorial de {nume}! es {fac}")