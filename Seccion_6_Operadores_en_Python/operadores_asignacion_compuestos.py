print('*** Operadores Asignacion Compuestos ***')
a, b = 10, 15
print(f'Valor inicial a: {a}, b: {b}')

# Operador conmpuesto de suma +=
a +=b # a =a + b
print(f'Operador a+= b es: {a}')

# Operador compuesto de resta -=
a = 10 # Reiniciamos la variable a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

# Operador compuesto de multiplicación
a = 10 # Reiniciamos el valor de a
a *= b
print(f'Operador a *= b es: {a}')

# Operador compuesto de division /=
a = 10 # Reiniciamos el valor de a
a /= b # a = a / b
print(f'Operador a /= b es: {a:.2f}') # ":.2f" es para que el valor de esa variable tenga solo 2 decimales
