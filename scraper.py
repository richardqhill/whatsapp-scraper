from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()
        self.group_chat_elems, self.group_chat_names = self.grab_group_chats()

    def start_driver(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')
        self.driver.get('https://web.whatsapp.com/')

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "app")))

    def quit(self):
        self.driver.quit()

    def grab_group_chats(self):


        element = self.driver.find_elements(By.CSS_SELECTOR, '#pane-side > div > div > div > div:nth-child(1) > div > div > div._3j7s9 > div._2FBdJ > div._25Ooe > span')
        element[0].click()

        return

        self.group_chat_elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "_3j7s9", " " ))]')

        text_elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')
        group_chat_names = []
        for elem in text_elems:
            group_chat_names.append(elem.text)
        return group_chat_names



    def grab_message_bodies_from_thread(self):

        return
        self.group_chat_elems[0].click()

        elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "invisible-space", " " ))]')

        print("debug")


if __name__ == "__main__":
    scraper = WhatsAppScraper()
    scraper.grab_group_chats()

    # scraper.grab_message_bodies_from_thread()

    scraper.quit()




