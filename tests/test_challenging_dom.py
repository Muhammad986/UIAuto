from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL_CITE
import time

def test_challenging_dom(browser):
    browser.get(URL_CITE)
    browser.find_element(By.LINK_TEXT, "Challenging DOM").click()

    buttons = [
        (By.XPATH, '//a[@class="button"]'),
        (By.XPATH, '//a[@class="button alert"]'),
        (By.XPATH, '//a[@class="button success"]')
    ]

    for button_locator in buttons:
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(button_locator))
        button.click()
        time.sleep(2) # Wait for 2 seconds before clicking the next button