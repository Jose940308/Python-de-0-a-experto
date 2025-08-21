#Inmutabilidad en cadenas, no podemos modificar ningun de los caracteres
cadena1 = 'Hola Mundo'
#cadena1[0] = 'h' #Genera un error.
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)

