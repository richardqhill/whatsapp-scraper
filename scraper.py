from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()

    def start_driver(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')
        self.driver.get('https://web.whatsapp.com/')

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "app")))

    def quit(self):
        self.driver.quit()

    def grab_group_chats(self):

        # TODO: Do something better than hard code select the first conversation

        # TODO: I want a better way to select the items in this list, in case things shift around while scraping

        element = self.driver.find_elements(By.CSS_SELECTOR, '#pane-side > div > div > div > div:nth-child(1) > div > div > div._3j7s9 > div._2FBdJ > div._25Ooe > span')
        element[0].click()

    def grab_message_bodies_from_thread(self):

        # TODO: Add code to scroll up to the top or at least scroll up for a while

        # TODO: grab message timestamps?
        # TODO: grab day from the window floating thing

        elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "ZhF0n", " " ))]')

        message_bodies = []
        for elem in elems:
            message_bodies.append(elem.text)

        print(message_bodies)


if __name__ == "__main__":
    scraper = WhatsAppScraper()
    scraper.grab_group_chats()

    scraper.grab_message_bodies_from_thread()

    scraper.quit()




