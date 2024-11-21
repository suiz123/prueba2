import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
 
class CalculadoraTests(unittest.TestCase):
    def setUp(self):
        # Configura el WebDriver (aquí se usa Chrome; ajusta según tu navegador)
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/calculadora/")
        time.sleep(1)  # Espera un momento para cargar la página
 
    def test_suma(self):
        driver = self.driver
        driver.find_element(By.NAME, "num1").send_keys("10")
        driver.find_element(By.NAME, "num2").send_keys("5")
        Select(driver.find_element(By.NAME, "operacion")).select_by_value("suma")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        
        # Verifica el resultado
        resultado = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Resultado: 15.0", resultado)
 
    def test_resta(self):
        driver = self.driver
        driver.find_element(By.NAME, "num1").send_keys("10")
        driver.find_element(By.NAME, "num2").send_keys("5")
        Select(driver.find_element(By.NAME, "operacion")).select_by_value("resta")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        
        resultado = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Resultado: 5.0", resultado)
 
    def test_multiplicacion(self):
        driver = self.driver
        driver.find_element(By.NAME, "num1").send_keys("10")
        driver.find_element(By.NAME, "num2").send_keys("5")
        Select(driver.find_element(By.NAME, "operacion")).select_by_value("multiplicacion")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        
        resultado = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Resultado: 50.0", resultado)
 
    def test_division(self):
        driver = self.driver
        driver.find_element(By.NAME, "num1").send_keys("10")
        driver.find_element(By.NAME, "num2").send_keys("0")
        Select(driver.find_element(By.NAME, "operacion")).select_by_value("division")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(1)
        
        resultado = driver.find_element(By.TAG_NAME, "h2").text
        self.assertIn("Resultado: Error", resultado)
 
    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()