from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import re

class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()
        self.group_chat_elements = self.grab_group_chats()

    def start_driver(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')
        self.driver.get('https://web.whatsapp.com/')

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located((By.ID, "app")))

    def quit(self):
        self.driver.quit()

    def grab_group_chats(self):

        # TODO: Be able to grab all conversations if there is a scrollbar in conversations

        return self.driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')

    def grab_urls_from_threads(self):

        urls = []

        for group_chat in self.group_chat_elements:
            group_chat.click()

            # TODO: Add code to scroll up to the top or at least scroll up for a while


            # TODO: grab message timestamps?
            # TODO: grab day from the window floating thing

            chat_bubble_elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "ZhF0n", " " ))]')

            for chat_bubble in chat_bubble_elems:

                temp = chat_bubble.get_attribute("data-pre-plain-text")

                message_urls = []
                for link in chat_bubble.find_elements_by_xpath('.//a'):
                    url = link.get_attribute('href')
                    if url not in urls:
                        message_urls.append(url)

                for timestamp in chat_bubble.find_elements_by_xpath('.//*[contains(concat( " ", @class, " " ), concat( " ", "ZhF0n", " " ))]'):
                    ts = timestamp.get_attribute("data-pre-plain-text")
                    print(timestamp.text)


                # main > div._3zJZ2 > div > div > div._9tCEa > div:nth-child(10) > div > div.Tkt2p > div._2f-RV > div > span._3EFt_

                if len(message_urls) != 0:
                    urls.extend(message_urls)

        print(urls)











if __name__ == "__main__":
    scraper = WhatsAppScraper()
    scraper.grab_group_chats()

    scraper.grab_urls_from_threads()

    scraper.quit()




