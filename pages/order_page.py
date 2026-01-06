from .base_page import BasePage

class OrderPage(BasePage):
    def fill_first_page(self, name, surname, address, phone):
        self.send_keys(("xpath", "//input[@placeholder='* Имя']"), name)
        self.send_keys(("xpath", "//input[@placeholder='* Фамилия']"), surname)
        self.send_keys(("xpath", "//input[@placeholder='* Адрес: куда привезти заказ']"), address)
        self.click(("xpath", "//input[@placeholder='* Станция метро']"))
        self.click(("xpath", "//li[@data-index='0']"))
        self.send_keys(("xpath", "//input[@placeholder='* Телефон: на него позвонит курьер']"), phone)
        self.click(("xpath", "//button[text()='Далее']"))
    
    def fill_second_page(self, comment=""):
        self.click(("xpath", "//input[@placeholder='* Когда привезти самокат']"))
        self.click(("xpath", "//div[contains(@class, 'react-datepicker__day--today')]"))
        self.click(("xpath", "//div[text()='* Срок аренды']"))
        self.click(("xpath", "//div[text()='сутки']"))
        self.click(("id", "black"))
        if comment:
            self.send_keys(("xpath", "//input[@placeholder='Комментарий для курьера']"), comment)
        self.click(("xpath", "(//button[text()='Заказать'])[2]"))
    
    def confirm_order(self):
        self.click(("xpath", "//button[text()='Да']"))
    
    def is_order_success(self):
        return self.is_displayed(("xpath", "//div[contains(text(), 'Заказ оформлен')]"))