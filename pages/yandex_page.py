from .base_page import BasePage


class YandexPage(BasePage):
    def wait_for_real_page_load(self, timeout=15):
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url not in ["about:blank", ""]
        )
    
    def is_on_yandex_or_dzen(self):
        current_url = self.get_current_url().lower()
        return any(keyword in current_url for keyword in ["yandex", "dzen"])