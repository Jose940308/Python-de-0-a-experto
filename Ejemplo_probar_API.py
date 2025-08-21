import requests

# 1. Definir la URL base de la API y el endpoint a probar
BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts"

# 2. Construir la URL completa para la peticion
url = f"{BASE_URL}{ENDPOINT}"

# 3. Enviar una peticion GET a la API
# Usamos un bloque try-except para manejar posibles errores de red
try:
    response = requests.get(url)
    print(f"Peticion GET a la URL: {url}")
    print(f"Codigo de estado de la respuesta: {response.status_code}")

    # 4. Validar el codigo de estado de la respuesta
    # El codigo 200 significa que la peticion fue exitosa
    assert response.status_code == 200, f"Error: Se esperaba un codigo 200, pero se recibio {response.status_code}"
    print("Validacion del codigo de estado exitosa. ✅")

    # 5. Validar el contenido de la respuesta
    # La API debe devolver una lista de publicaciones en formato JSON
    posts = response.json()
    assert isinstance(posts, list), f"Error: Se esperaba una lista, pero se recibio {type(posts)}"
    assert len(posts) > 0, "Error: La lista de publicaciones esta vacia"
    print(f"Validacion del contenido exitosa. Se recibieron {len(posts)} publicaciones. ✅")

    # 6. Validar un elemento especifico de la lista
    # Verificamos la primera publicacion para asegurarnos de que tiene las llaves correctas
    first_post = posts[0]
    assert "userId" in first_post, "Error: Falta la llave 'userId' en la publicacion"
    assert "id" in first_post, "Error: Falta la llave 'id' en la publicacion"
    assert "title" in first_post, "Error: Falta la llave 'title' en la publicacion"
    print("Validacion de la estructura de la primera publicacion exitosa. ✅")

    print("\n¡Todas las pruebas pasaron exitosamente!")

except requests.exceptions.RequestException as e:
    print(f"Error de conexion al intentar acceder a la API: {e}")