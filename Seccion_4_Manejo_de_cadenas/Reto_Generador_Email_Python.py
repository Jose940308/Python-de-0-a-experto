#Crear un programa generar un email a partir de los siguientes datos:
# Nombre: Jose Lopez Alvarez
# Empresa: Desempleado Coporation
# Dominio: com.mx
# Resultado final email: jose.lopez.alvarez@desempleadocorporation.com.mx (todo en minusculas)
#Imprimir el nombre del usuario, nombre del usuario normalizado, espacio, nombre de la empresa, extension del dominio y dominio normalizado, un espacio y el Email final generado

#Comenzando programa definiendo variables
nombre = 'Jose Lopez Alvarez'
empresa = 'Industrial Corporation'
dominio = '.com.mx'
#Normalizando datos
nombre_norm = nombre.split('.')
empresa_norm = empresa.strip()
email = nombre.lower() + empresa.lower()

print(nombre_norm)
#print(f'Nombre: {nombre} \n Empresa: {empresa_norm} \n Email generado: {email}')
