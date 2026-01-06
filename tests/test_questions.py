import pytest
import allure
from pages.main_page import MainPage

class TestQuestions:
    @pytest.mark.parametrize("index", range(8))
    @allure.title("Вопрос №{index}")
    def test_question(self, driver, index):
        page = MainPage(driver)
        page.open()
        page.click_question(index)
        answer = page.get_answer_text(index)
        assert len(answer.strip()) > 0