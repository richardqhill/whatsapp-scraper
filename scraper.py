from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()
        self.group_chat_names = self.grab_group_chat_names()

    def start_driver(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')
        self.driver.get('https://web.whatsapp.com/')

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
        except:
            print("Yo, you didn't scan it fast enough (10 seconds)....")

    def quit(self):
        self.driver.quit()

    def grab_group_chat_names(self):
        elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')
        group_chat_names = []
        for elem in elems:
            group_chat_names.append(elem.text)
        return group_chat_names

    def select_thread(self, thread_name):

        elem = self.driver.find_element_by_link_text(thread_name)

        print("debug")

        pass



    def grab_message_bodies_from_thread(self, thread_name):

        self.select_thread(thread_name)

        elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "invisible-space", " " ))]')

        print("debug")


if __name__ == "__main__":
    scraper = WhatsAppScraper()

    temp = scraper.group_chat_names
    print(temp)

    #scraper.grab_message_bodies_from_thread(temp[0])


