'''Crear un programa para solicitar algunos valores importantes para una receta de cocina.
Los valores que debe introducir el usuario por la consola son:
Mandar a imprimir el título *** Receta de Cocina ***
Nombre de la receta
Ingredientes
Tiempo de preparacion en minutos (se debe convertir un valor de tipo entero)
La dificultad de la receta (Fácil, Medio, Difícil)
Mandar a imprimir varios guiones o un salto de linea para separar los datos
Mandar a imprimir los valores introducidos por el usuario.'''

print('*** Receta de Cocina ***')

# Paso 1. Definiendo variables para la entrada de datos en la consola
nombre_receta = input('Introduce el nombre de la receta: ')
ingredientes = input('Introduce los ingredientes de tu receta: ')
tiempo_prep = int(input('Ingresa el tiempo de preparación en minutos: ')) #Convertir a entero
dificultad_receta = input('Ingresa la dificultad (facil, medio o dificil): ')

# Paso 2. Imprimiendo los datos ingresados por el usuario
print(f'\nDatos de la receta')
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingrese los ingredientes: {ingredientes}')
print(f'Duración de preparación: {tiempo_prep}')
print(f'Ingrese la dificultad: {dificultad_receta}')
print(f'\n')
print('Muchas gracias por utilizar nuestra terminal')