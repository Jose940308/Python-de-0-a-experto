'''fruits = ['apple', 'bananna', 'peach']
for index, fruta in enumerate(fruits):
    print(index, fruta)
'''


# Por cada bannana dentro del array, elevar x al cubo
fruits = ['apple', 'bannana', 'peach', 'bannana']
x = 0
if 'bannana' in fruits:
    x+=1
    print('Si lo encontró xD')
print(x)


# Estacionamiento
estacionamiento = ['polo', 'polo', 'moto', 'vocho']
print(len(estacionamiento))

print(f'Irele werito estos son los polos: {estacionamiento.count('polo')}\nY estas son el num de motos papu: {estacionamiento.count('moto')}')

# Añadiendo un BMW al estacionamiento
estacionamiento.insert(3,'BMW')
print(estacionamiento)

#Eliminando uno de los polos del estacionamiento
estacionamiento.remove('polo')
print(estacionamiento)

# Encontrando la posicion de BMW en el estacionamiento
print(estacionamiento.index('BMW'))

# Reacomodando el estacionamiento en el sig orden: Vocho, BMW, Moto y Polo
# Originalmente esta:                             ['polo', 'moto', 'BMW', 'vocho']
estacionamiento.reverse()
print(estacionamiento)

estacionamiento.index