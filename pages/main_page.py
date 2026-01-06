from .base_page import BasePage

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"
    
    def open(self):
        self.driver.get(self.URL)
        try:
            self.click(("id", "rcc-confirm-button"))
        except:
            pass
    
    def click_question(self, index):
        self.click(("id", f"accordion__heading-{index}"))
    
    def get_answer_text(self, index):
        return self.get_text(("id", f"accordion__panel-{index}"))
    
    def click_top_order(self):
        self.click(("xpath", "//button[text()='Заказать']"))
    
    def click_bottom_order(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(("xpath", "(//button[text()='Заказать'])[2]"))
    
    def click_scooter_logo(self):
        self.click(("xpath", "//a[@href='/']"))
    
    def click_yandex_logo(self):
        self.click(("xpath", "//a[@href='//yandex.ru']"))