import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.yandex_page import YandexPage


class TestOrderTopButtonFirstDataset:
    @allure.title("Заказ самоката через верхнюю кнопку с первым набором данных")
    def test_order_scooter_top_button_first_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page("Иван", "Иванов", "ул. Пушкина, д. 1", "89998887766")
        order_page.fill_second_page("Позвонить за час")
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


class TestOrderTopButtonSecondDataset:
    @allure.title("Заказ самоката через верхнюю кнопку со вторым набором данных")
    def test_order_scooter_top_button_second_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page("Мария", "Петрова", "пр. Ленина, д. 10", "89997776655")
        order_page.fill_second_page("Оставить у двери")
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


class TestOrderBottomButtonFirstDataset:
    @allure.title("Заказ самоката через нижнюю кнопку с первым набором данных")
    def test_order_scooter_bottom_button_first_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page("Иван", "Иванов", "ул. Пушкина, д. 1", "89998887766")
        order_page.fill_second_page("Позвонить за час")
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


class TestOrderBottomButtonSecondDataset:
    @allure.title("Заказ самоката через нижнюю кнопку со вторым набором данных")
    def test_order_scooter_bottom_button_second_dataset(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)
        order_page.wait_for_order_form_to_load()
        order_page.fill_first_page("Мария", "Петрова", "пр. Ленина, д. 10", "89997776655")
        order_page.fill_second_page("Оставить у двери")
        order_page.confirm_order()
        assert order_page.is_order_success_displayed()


class TestScooterLogo:
    @allure.title("Проверка перехода на главную страницу по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_scooter_logo()
        assert main_page.is_on_main_page()


class TestYandexLogo:
    @allure.title("Проверка перехода на Дзен по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        main_page.wait_for_new_window([main_window])
        windows = main_page.get_window_handles()
        new_window = windows[-1]
        main_page.switch_to_window(new_window)
        yandex_page = YandexPage(driver)
        yandex_page.wait_for_real_page_load()
        assert yandex_page.is_on_yandex_or_dzen()
        yandex_page.close_current_window()
        main_page.switch_to_window(main_window)