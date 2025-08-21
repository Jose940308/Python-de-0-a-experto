'''Se solicita crear un sistema para generar un ID unico para cada persona.
    Imprimir el titulo del programa.
    El sistema debe solicitar al usuario:
        -Nombre
        -Apellido
        -Año de nacimiento (YYYY)
    Con los datos recibidos, el sistema deberá realizar lo siguiente:
        1. Del valor recibido de nombre, usar sólo las 2 primeras letras y convertirlas a mayúsculas.
        2. Del valor de apellido, usar las 2 primeras letras y convertirlas a mayúsculas
        3. Del valor de año, tomar los 2 últimos Digitos.
    
    Además el sistema deberá generar un valor aleatorio de 4 dígitos, con ayuda de la función randint.
    Finalmente, con los datos obtenidos generar un ID único uniendo los valores como el sig ejemplo:
        Nombre --> Juan --> JU
        Apellido --> Perez --> PE
        Año Nacimiento --> 1995 --> 95
        Valor aleatorio --> randit --> 7326
'''
from random import randint
print('--- Sistema Generador de ID único ---')
print('\nPor favor, ingrese los datos solicitados')

# Paso 1. Definiendo variables de entrada.
nombre_usuario = input('Ingresa tu nombre(s) : ')
apellido_usuario = input('Ingresa tus apellidos: ')
año_nacimiento = input('Ingresa tu año de nacimiento (YYYY): ')
ID_aleatirio = randint(1000,9999)
ID_aleatirio = str(ID_aleatirio)   

# Paso 2. Normalizar la información
nombre_usuario_mayusculas = nombre_usuario.upper()
apellido_usuario_mayusculas = apellido_usuario.upper()
ID_generado = nombre_usuario_mayusculas[:2] + apellido_usuario_mayusculas[:2] + año_nacimiento[-2:] + ID_aleatirio

#Paso 3. Imprimiendo el ID generado
print(f'\nID Gnerado: ',ID_generado)




