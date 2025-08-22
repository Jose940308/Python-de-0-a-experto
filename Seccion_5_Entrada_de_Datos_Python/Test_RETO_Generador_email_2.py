# Script para pruebas unitarias del programa RETO_Generador_email_2

import pytest
from DEMO_RETO_Generador_email_2 import generar_correo

def test_generar_correo():
    # Caso de prueba 1: Datos normales
    nombre = "Juan Carlos"
    apellidos = "Gómez Lara"
    compañia = "Global Mentoring"
    extension = ".com.mx"
    resultado_esperado = "juan.carlos.gomez.lara@globalmentoring.com.mx"
    assert generar_correo(nombre, apellidos, compañia, extension) == resultado_esperado

    # Caso de prueba 2: Datos con espacios extra
    nombre = "  Ana Maria  "
    apellidos = "  Perez  "
    compañia = "  Tech Corp  "
    extension = "  .org  "
    resultado_esperado = "ana.maria.perez@techcorp.org"
    assert generar_correo(nombre, apellidos, compañia, extension) == resultado_esperado

    # Caso de prueba 3: Datos en mayúsculas
    nombre = "PEDRO"
    apellidos = "LOPEZ"
    compañia = "MY COMPANY"
    extension = ".NET"
    resultado_esperado = "pedro.lopez@mycompany.net"
    assert generar_correo(nombre, apellidos, compañia, extension) == resultado_esperado