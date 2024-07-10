#solicito al usuario me de el numero de la tabla de multiplicar que deseee
tab = int(input("seleccione el numero de la tabla de multiplicar: "))
#bucle para mostrar la tabla de multiplicar
for i in range(1, 12+1):
  #calculo el resultado de la multiplicacion
  t = tab * i
  #muestro el resultado de la multiplicacion
  print(i, "x", tab, "=", t)