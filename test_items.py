from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_find_button_add_to_chart( browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    # time.sleep(30)
    assert WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-add-to-basket"))), "кнопки добавить в корзину нет на странице"




