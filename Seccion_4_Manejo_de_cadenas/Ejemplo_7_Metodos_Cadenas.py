#Metodos de cadenas, definiendo variables:
cadena1 = 'Hola Mundo'
cadena2 = ' Juan Perez '

print(f'Cadena original: {cadena1}')
mayusculas = cadena1.upper()
#Convirtiendo la cadena en mayusculas:
print(f'Cadena mayusculas: {mayusculas}')
#Conviertiendo la cadena en minusculas:
print(f'Cadena en minusculas: {cadena1.lower()}')

#Imprimiendo la cadena2 sin modificacion
print(f'Cadena con espacios: {cadena2}')
#Imprimiendo la cadena2 eliminando los espacios al inicio y al final, nos sirve para limpiar informacion
print(f'Cadena sin espacios: {cadena2.strip()}')

