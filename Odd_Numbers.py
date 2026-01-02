def oddNumbers(l, r):
    # Nota: En tu fragmento, l y r eran 'input_1' y 'input_2'
    resultado = [] 

    # Iterar sobre todos los números en el rango [l, r], INCLUYENDO r.
    # Por eso usamos r + 1, ya que range() es exclusivo en el límite superior.
    for numero in range(l, r + 1):
        
        # Lógica de número impar: El residuo de la división por 2 es 1.
        if numero % 2 != 0: 
            resultado.append(numero)
            
    return resultado

# --- Prueba con Casos Extremos (Como lo hace HackerRank) ---
# Caso 1: l par, r impar (2, 5) -> Esperado [3, 5]
# print(oddNumbers(2, 5)) 

# Caso 2: l impar, r impar (3, 9) -> Esperado [3, 5, 7, 9]
# print(oddNumbers(3, 9)) 

# Caso 3: l=r (1, 1) -> Esperado [1]
# print(oddNumbers(1, 1))