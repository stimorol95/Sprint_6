import pytest
import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:
    @pytest.mark.parametrize("button", ["top", "bottom"])
    @pytest.mark.parametrize("data", [
        {"name": "Иван", "surname": "Иванов", "address": "ул. Пушкина, д. 1", "phone": "89998887766", "comment": ""},
        {"name": "Мария", "surname": "Петрова", "address": "пр. Ленина, д. 10", "phone": "89997776655", "comment": "Оставить"}
    ])
    @allure.title("Заказ самоката")
    def test_order_scooter(self, driver, button, data):
        main = MainPage(driver)
        main.open()
        
        if button == "top":
            main.click_top_order()
        else:
            main.click_bottom_order()
        
        order = OrderPage(driver)
        order.fill_first_page(data["name"], data["surname"], data["address"], data["phone"])
        order.fill_second_page(data["comment"])
        order.confirm_order()
        
        assert order.is_order_success()
    
    @allure.title("Логотип Самоката")
    def test_scooter_logo(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_scooter_logo()
        assert "qa-scooter.praktikum-services.ru" in driver.current_url
    
    @allure.title("Логотип Яндекса")
    def test_yandex_logo(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_yandex_logo()
        time.sleep(3)
        
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            current_url = driver.current_url
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            assert "yandex" in current_url or "dzen" in current_url
        else:
            assert "yandex" in driver.current_url or "dzen" in driver.current_url