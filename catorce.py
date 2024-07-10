#pido al usuario que ingrese una cadena
cad = input("Ingresa la cadena a verificar: ")
#verifico si la cadena es palindromo
if cad == cad[::-1]:
  #si es palindromo muestro un mensaje
  print("Es palindromo")
else:
  #si no es palindromo muestro un mensaje
  print("No es palindromo")