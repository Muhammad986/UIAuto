from selenium.webdriver.common.by import By
from config import URL_CITE, URL_CITE_AUTH
import time

def test_basic_auth(browser):
    """Тест авторизации на странице Basic Auth"""
    browser.get(URL_CITE)  # Use URL_CITE from config.py
    assert "The Internet" in browser.title
    time.sleep(2)

    browser.find_element(By.LINK_TEXT, "Basic Auth").click()
    time.sleep(2)
    
    browser.get(URL_CITE_AUTH)
    element = browser.find_element(By.TAG_NAME, "p")
    time.sleep(3)
    assert "Congratulations" in element.text