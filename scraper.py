from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()
        self.group_chat_elements = self.grab_group_chats()

    def start_driver(self):
        self.driver = webdriver.Chrome('./chromedriver_mac')
        self.driver.get('https://web.whatsapp.com/')

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "app")))

    def quit(self):
        self.driver.quit()

    def grab_group_chats(self):

        # TODO: Be able to grab all conversations if there is a scrollbar in conversations

        return self.driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')

    def grab_message_bodies_from_thread(self):

        # TODO: Add code to scroll up to the top or at least scroll up for a while

        # TODO: grab message timestamps?
        # TODO: grab day from the window floating thing

        message_bodies = []

        for group_chat in self.group_chat_elements:
            group_chat.click()

            message_text_elems = self.driver.find_elements(By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "ZhF0n", " " ))]')

            for elem in message_text_elems:
                message_bodies.append(elem.text)

        print(message_bodies)


# TODO: parse message bodies to determine if URL

if __name__ == "__main__":
    scraper = WhatsAppScraper()
    scraper.grab_group_chats()

    scraper.grab_message_bodies_from_thread()

    scraper.quit()




