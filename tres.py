#pido al usuario un numero para validar
num = int(input("Ingresa el numero a verificar: "))
#verifico si el numero es par
if num % 2 == 0 :
  #si es par muestro un mensaje
  print(f"{num}, es par")
else:
  #si es impar muestro un mensaje
  print(f"{num} es falso")