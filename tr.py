from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="col-sm-6 product_main"]/h1'))
    )
finally:
    driver.quit()