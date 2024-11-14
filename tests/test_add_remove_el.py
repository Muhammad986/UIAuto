from selenium.webdriver.common.by import By
from config import URL_CITE # Assuming you have a config.py file with URL_CITE defined
import time

def test_add_and_remove_element(browser):
    """Test adding and removing elements on the Add/Remove Elements page"""

    browser.get(URL_CITE)  # Use URL_CITE from config.py
    assert "The Internet" in browser.title
    time.sleep(2)

    add_remove_link = browser.find_element(By.LINK_TEXT, "Add/Remove Elements")
    add_remove_link.click()

    # Click the add button multiple times
    add_button = browser.find_element(By.XPATH, "//*[@id='content']/div/button[text()='Add Element']")
    for _ in range(5):
        add_button.click()
    
    time.sleep(2)
    
    # Count the number of added elements
    elements = browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
    assert len(elements) == 5

    # Remove elements iteratively
    for _ in range(3):
        remove_button = browser.find_element(By.XPATH, "//*[@id='elements']/button[text()='Delete']")
        remove_button.click()

    time.sleep(2)
    
    # Count the remaining elements
    elements = browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
    assert len(elements) == 2