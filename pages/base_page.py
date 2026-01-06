from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find(self, locator, timeout=10):
        with allure.step(f"Найти элемент"):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
    
    def click(self, locator):
        with allure.step(f"Кликнуть"):
            self.find(locator).click()
    
    def send_keys(self, locator, text):
        with allure.step(f"Ввести текст"):
            element = self.find(locator)
            element.clear()
            element.send_keys(text)
    
    def get_text(self, locator):
        return self.find(locator).text
    
    def is_displayed(self, locator):
        try:
            return self.find(locator, timeout=3).is_displayed()
        except:
            return False