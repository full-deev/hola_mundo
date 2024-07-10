#muestro un menu para interactuar con el usuario
print("Según el menu mostrado vamos a realizar algunas operaciones, let's goo! ☻")
print('''\n
1- Suma
2- Resta
3- Producto
4- Division
''')
#pido al usuario que seleccione una opcion y lo guardo en una varibale
caso = int(input("Selecciona el numero de la operacion asignada: "))
#pido al usuario que ingrese dos numeros para realizar la operacion
numUno = int(input("Ingresa primer digito: "))
numDos = int(input("Ingresa segundo digito: "))
#realizo condiciones segun el menu 1
if caso == 1:
  tt = numUno + numDos
  print("el resultado de la operacion es: ", tt)
# condicion segun 2
elif caso == 2:
  tt = numUno - numDos
  print("el resultado de la operacion es: ", tt)
# condicion segun 3
elif caso == 3:
  tt = numUno * numDos
  print("el resultado de la operacion es: ", tt)
# condicion segun 4
elif caso == 4:
  tt = numUno / numDos
  print("el resultado de la operacion es: ", tt)