print('*** Sentencia if ***')

edad = int(input('Inserta tu edad: '))
if edad >= 21:
    print(f'Eres mayor de edad. Tienes {edad} años.')
elif 17 <= edad < 18:
    print(f'Sigues siendo menor de edad, tienes {edad}')
else: print(f'No eres mayor de edad. Tienes {edad} años.')