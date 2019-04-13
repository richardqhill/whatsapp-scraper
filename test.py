import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver_mac')  # Optional argument, if not specified will search path.

driver.get('https://web.whatsapp.com/')

# time.sleep(5)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
except:
    print("Yo, you didn't scan it fast enough....")


elems = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')



print("hi")


driver.quit()