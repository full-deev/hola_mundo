#el usuario ingresa un numero para verificar si es primo o
n = int(input("Ingresa un numero para conocer si es primo: "))
#verifico si el numero es primo mediante una funcion
def es_primo(n):
  #verifico si el numero es menor a 2
  if n < 2:
    return False
  #verifico si el numero es divisible entre 2
  for i in range(2,int(n/2)):
    #si es divisible entre 2 entonces no es primo
    if (n%i) == 0:

      return False
  return True
#llamo a la funcion y muestro su resultado.
es_primo(n)