#Crear un programa generar un email a partir de los siguientes datos:
# Nombre: Jose Lopez Alvarez
# Empresa: Desempleado Coporation
# Dominio: com.mx
# Resultado final email: jose.lopez.alvarez@desempleadocorporation.com.mx (todo en minusculas)
#Imprimir el nombre del usuario, nombre del usuario normalizado, espacio, nombre de la empresa, extension del dominio y dominio normalizado, un espacio y el Email final generado

#Comenzando programa definiendo variables
nombre_completo = ' Jose Lopez Alvarez '
empresa = 'Industrial Corporation'
dominio = '.com.mx'
#Normalizando datos
nombre_norm = nombre_completo.strip().lower().replace(' ', '.')
#nombre_norm = nombre_norm.replace(' ', '.')
empresa_norm = empresa.strip().lower().replace(' ', '')
dominio_email = f'@{empresa_norm}{dominio}'
email = f'{nombre_norm}{dominio_email}'


print('*** Generaddor de emails ***')
print(f' Nombre: {nombre_completo} \n Empresa: {empresa} \n Email generado: {email}')