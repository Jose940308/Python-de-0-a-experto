'''
Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda.

Se deben revisar las sig condiciones:
1) Si ha comprado mas de $1000 y es miembro --> Desc del 10%
    Imprimir el monto de la compra
    Imprimir un mensaje de que ha sido acreedor de un descuento
    Imprimir el monto del descuento
    Imprimir el monto total a pagar

2) Si sólo es miembro de la tienda --> Desc del 5%
    Imprimir el monto de la compra
    Imprimir un mensaje de que ha sido acreedor de un descuento
    Imprimir el monto del descuento
    Imprimir el monto total a pagar

3) SI no es miembro ni compró más de mil --> Desc del 0%
    Imprimir el monto de la compra
    Imprimir un mensaje de que NO ha sido acreedor de un descuento
    Imprimir un mensaje invitando a ser miembro de la tienda
    Imprimir el monto total a pagar
'''
# Iniciando programa
print('*** Sistema de Descuentos ***')

monto = float(input('Inserte el monto de su compra: '))
miembro = str(input('¿Es miembro de la tienda? SI/NO: '))

if miembro == 'SI' and monto >= 1000:
    descuento = monto * 0.10
    monto_total = monto - descuento
    print('Felicidades, has obtenido un 10% de descuento')
    print(f'Monto del descuento: {descuento:.2f}')
    print(f'Monto final de la compra con descuento: {monto_total}')
elif miembro == 'SI'and monto < 1000:
    print(f'Tu compra fue de {monto}')
    descuento = monto * 0.05
    monto_total = monto - descuento
    print('Felicidades, has obtenido un 5% de descuento')
    print(f'Monto del descuento: {descuento:.2f}')
    print(f'Monto final de la compra con descuento: {monto_total}')
else:
    print('Lo siento, no tuviste ningún tipo de descuento \n Te invitamos a hacerte miembro de la tienda ')
    print(f'Monto final de la compra: {monto}')



