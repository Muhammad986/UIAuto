from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import time
from config import URL_CITE

##@pytest.mark.test

    
def test_broken_images(browser):
    """Проверяет наличие сломанных изображений на странице"""

    browser.get(URL_CITE)
    assert "The Internet" in browser.title
    
    browser.find_element(By.LINK_TEXT, "Broken Images").click()

    broken_images = get_img(browser)
    time.sleep(2)
    print(f'Brokeen: {broken_images}')
    assert broken_images, f"Found broken images: {broken_images}"
    
def test_no_broken_images(browser):
    """Проверяет отсутствие сломанных изображений на странице"""

    browser.get(URL_CITE)
    assert "The Internet" in browser.title
    
    browser.find_element(By.LINK_TEXT, "Broken Images").click()
    
    broken_images = get_img(browser)
    time.sleep(2)
    print(f'Brokeen: {broken_images}')
    assert not broken_images, f"Found broken images: {broken_images}"
   
 
def get_img(browser):
    # Получаем HTML-код страницы и парсим его
    html_content = browser.page_source
    soup = BeautifulSoup(html_content, 'html.parser')


    images = soup.find_all('div', class_='example')[0].find_all('img')

    broken_images = []
    for img in images:
        src = img.get('src')
        base_url = browser.current_url #Получает текущий URL страницы из объекта Selenium webdriver.
        full_url = urljoin(base_url, src) #Создает полный URL изображения.
        try:
            response = requests.get(full_url) #Отправляет HTTP-запрос к URL изображения.
            if response.status_code != 200:
                broken_images.append(src) # сохраняем исходный src, а не full_url для наглядности.
        except requests.exceptions.RequestException:
            broken_images.append(src)
            
    return broken_images