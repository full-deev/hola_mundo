#solicito al usuario ingrese los valoores del radio
radio = float(input("Ingresa el valor del radio: "))
#asigno a una variable el valor de pi
pii = 3.141592653589793
#calculo el area del circulo
aCirculo = pii * radio ** 2
#redondeo el resultado a solo 2 decimales
aCirculo = round(aCirculo, 2)
#muestro el resultado
print(f"El area del circulo con radio {radio}, es {aCirculo}")