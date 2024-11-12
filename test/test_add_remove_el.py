import pytest
from selenium.webdriver.common.by import By
import time

from config import URL_CITE # Assuming you have a config.py file with URL_CITE defined

@pytest.fixture
def open_browser(browser):
    browser.get(URL_CITE) # Use URL_CITE from config.py
    yield browser # Yield the browser for the test to use
    browser.quit() # Close the browser after the test is finished

def test_add_and_remove_element(open_browser): # Use open_browser fixture
    assert "The Internet" in open_browser.title # Check the expected title
    time.sleep(1)
    
    open_browser.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
    time.sleep(1)
    
    # Click the add button multiple times
    add_button = open_browser.find_element(By.XPATH, "//*[@id='content']/div/button[text()[.='Add Element']]")
    for i in range(5):
        add_button.click()
        print(f'i:{i}')##########################
    time.sleep(3)
    
    # Count the number of elements
    elements = open_browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
    print(len(elements))#######################
    assert len(elements) == 5 # Check that 3 elements have been added
    

    # Click the remove button (with explicit wait)
    #Кнопку я не вывел из for, так как теряет свой xpath после 1го использования
    for i in range(3):
        open_browser.find_element(By.XPATH, "//*[@id='elements']/button[text()='Delete']").click()
        time.sleep(1)

    # Count the number of elements again (should be 2 now)
    elements = open_browser.find_elements(By.XPATH, '//*[@id="elements"]/button')
    assert len(elements) == 2 # Check that 1 element has been removed


if __name__ == "__main__": # Correct condition for running tests
    pytest.main() 
