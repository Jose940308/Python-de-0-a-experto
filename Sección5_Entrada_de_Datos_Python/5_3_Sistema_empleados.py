print('*** Sistema de empleados ***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('¿Es jefe de departamento? (Si/No): ')

#Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si' #Con el comparador == 'si' lo convertimos a un booleano

#Vamos a imprimir los valores del empleado
print(f'\nDatos del empleado:')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')  # Formateamos el salario a dos decimales de un tipo flotante
print(f'¿Es jefe de departamento?: {es_jefe_departamento}') 