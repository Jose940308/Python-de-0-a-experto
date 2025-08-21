#Python no restringe las constantes si ponemos todo en mayúsculas, pero por buenas prácticas, se recomienda que las constantes sean en mayúsculas.
print('*** Constantes en Python ***')

PI = 3.1416
print('El valor de PI es', PI)

NOMBRE_BASE_DATOS = 'Clientes_db'
print('Nombre de la base de datos', NOMBRE_BASE_DATOS)

#Esto no se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = 'Listado_clientes_db'
print('No cambiar el valor de una constante', NOMBRE_BASE_DATOS)

