# 1. Definicion de la CLASE 'Vehiculo'
# Esta es la plantilla o el plano para crear vehiculos.
class Vehiculo:
    # El constructor (__init__) inicializa los atributos del objeto.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Metodo (comportamiento) de la clase padre
    def arrancar(self):
        return f"El {self.marca} {self.modelo} esta arrancando."

    def acelerar(self):
        return f"El {self.marca} {self.modelo} esta acelerando."

# ---

# 2. Creacion de OBJETOS a partir de la clase 'Vehiculo'
# Cada objeto es una instancia unica de la clase.
coche_de_gasolina = Vehiculo("Ford", "Mustang")
coche_de_diesel = Vehiculo("Volkswagen", "Passat")

print("---")
print("Ejemplo de Objeto:")
print(coche_de_gasolina.acelerar())
print(coche_de_diesel.arrancar())
print("---")

# ---

# 3. Herencia: Creando una nueva clase 'CocheElectrico' que hereda de 'Vehiculo'
# Esta clase hija hereda los atributos y metodos de la clase padre 'Vehiculo'.
class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, bateria):
        # Con 'super()', llamamos al constructor de la clase padre para reutilizar su codigo.
        super().__init__(marca, modelo)
        self.bateria = bateria  # Atributo especifico de la clase hija

    # Nuevo metodo exclusivo de la clase hija
    def cargar_bateria(self):
        return f"El {self.marca} {self.modelo} con {self.bateria} esta cargando."

# ---

# 4. Polimorfismo: Redefiniendo el metodo 'acelerar()' de la clase padre
# El mismo metodo 'acelerar' tiene un comportamiento diferente en esta clase.
    def acelerar(self):
        return f"El {self.marca} {self.modelo} acelera con un torque instantaneo."

# Creacion de un nuevo objeto de la clase hija
coche_electrico = CocheElectrico("Tesla", "Model Y", "75 kWh")

print("---")
print("Ejemplo de Herencia:")
print(coche_electrico.arrancar())  # Hereda este metodo del padre
print(coche_electrico.cargar_bateria()) # Metodo propio de la clase hija
print("---")

print("---")
print("Ejemplo de Polimorfismo:")
print(coche_de_gasolina.acelerar())  # Ejecuta el metodo del Vehiculo normal
print(coche_electrico.acelerar())    # Ejecuta el metodo sobreescrito del CocheElectrico
print("---")