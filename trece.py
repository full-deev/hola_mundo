#pido al usuario que ingrese el texto
texto = input("Ingresa el texto a contar: ")
#paso el texto a minusculas
texto = texto.lower()
#asigno las vocales en una variable
vocales = "aeiou"
#inicializo un contador en 0
contador = 0
#bucle para contar las vocales
for i in texto:
  #verifico si el caracter es una vocal
  if i in vocales:
    #si es vocal sumo 1 al contador
    contador += 1
    #muestro el contador
print(f"el numero de vocales son {contador}")