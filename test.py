import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver_mac')  # Optional argument, if not specified will search path.

driver.get('https://web.whatsapp.com/');

time.sleep(5) # Let the user actually see something!

elems = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')




driver.quit()