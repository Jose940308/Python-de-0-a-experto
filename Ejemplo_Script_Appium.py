#Este es un ejemplo de como sería un script para probar la calculadora de una aplicación móvil usando Appium.
from Appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Paso 1 Configuracion del dispositivo y de la app
desired_caps ={
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'Android Emulator2',
        'appPackage': 'com.android.calculator2',
        'appActvity': '.Calculator'
    }

# Paso 2 Conectar Appium con el dispositivo
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Paso 3 Localizar y hacer clic en botones
driver.find_element(AppiumBy.ID, 'com.android.calculator2:id/digit_7').click()
driver.find_element(AppiumBy.ID, 'com.android.calculator2:id/op_add').click()
driver.find_element(AppiumBy.ID, 'com.android.calculator2:id/digit_8').click()
driver.find_element(AppiumBy.ID, 'com.android.calculator2:id/eq').click()

# Paso 4 Obtener y verificar el resultado
result_element = driver.find_element(AppiumBy.ID, 'com.android.calculator2:id/result')
assert result_element.text == '15', 'El resultado es incorrecto'

#Paso 5 Cerrar la sesión
driver.quit()
