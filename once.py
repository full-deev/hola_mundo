#defino un limite para sumar los numeros
nSuma = int(input("Ingresa el limite de numeros a contar desde el 1: "))
#inicializo la variable suma en 0
suma = 0
#bucle para sumar los numeros desde el 1 hasta el limite
for i in range(nSuma+1):
  #sumo los numeros
  suma += i
  #muestro el resultado de la suma
print("El total de la suma es: ",suma)