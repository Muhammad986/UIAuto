from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import URL_CITE

def test_checkboxes(browser):
    browser.get(URL_CITE)
    browser.find_element(By.LINK_TEXT, "Checkboxes").click()

    # Находим оба чекбокса
    checkboxes = browser.find_elements(By.XPATH, '//*[@id="checkboxes"]/input')

    # Функция для проверки и переключения состояния чекбокса
    def toggle_checkbox(checkbox):
        current_state = checkbox.is_selected()
        time.sleep(2)
        checkbox.click()
        assert checkbox.is_selected() != current_state, f"Состояние чекбокса не изменилось: {current_state}"
        time.sleep(1)

    # Проверяем и переключаем состояние каждого чекбокса
    for checkbox in checkboxes:
        toggle_checkbox(checkbox)
        toggle_checkbox(checkbox)  # Возвращаем в исходное состояние

    print("Тест на чекбоксы пройден успешно!")