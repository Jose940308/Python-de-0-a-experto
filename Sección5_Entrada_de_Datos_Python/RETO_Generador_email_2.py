'''
    Se solicita crear una nueva versuon del sistema generador de emails.
    Para generar el email se debe solicitar:
        -Nombre --> Ej. Juan Carlos
        -Apellidos --> Ej. Gómez Lara
        -Nombre de la empresa --> Ej. Global Mentoring
        -Extensión Dominio --> Ej. .com.mx
    El resultado debe ser: juan.carlos.gomez.lara@globalmentoring.com.mx
'''
print('--- Sistema generador de dirección de correo electrónico ---\n\nPor favor ingrese los datos solicitados')

# Definiendo las variables de entrada
nombre = input('Ingresa tu nombre(s): ')
apellidos = input('Ingresa tus apellidos: ')
compañia = input('Ingresa el nombre de la compañia: ')
extension = input('Ingresa la extensión del dominio del correo (e. .com.mx o .gob): ')

# Concatenando con el método join, normalizando datos e imprimiendo resultado final
correo = f'{'.'.join(nombre.strip().lower().split())}.{'.'.join(apellidos.strip().lower().split())}@{''.join(compañia.strip().lower().split())}{extension.strip().lower()}'
print('\nEsta es la dirección de tu correo electrónico: ', correo)
print('\n Muchas gracias por utilizar nuestra herramienta.')