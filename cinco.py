#Solicito al usuario que ingrese los numeros
nUno = int(input("Ingresa primer numero: "))
nDos = int(input("Ingresa segundo numero: "))
nTres = int(input("Ingresa tercer numero: "))
#condiciones para saber que numero es mayor numero 1
if nUno > nDos:
  #condicion para saber que numero es mayor numero 2
  if nUno > nTres:
    print(nUno)
  #condiciones por falso
  else:
    print(nTres)
else:
  if nDos > nTres:
    print(nDos)
  else:
    print(nTres)