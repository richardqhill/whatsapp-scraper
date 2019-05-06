from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from collections import Counter
from collections import defaultdict
from pathlib import Path
import json
import time


class WhatsAppScraper:
    def __init__(self):
        self.driver = None
        self.start_driver()
        self.group_chat_elements = self.grab_group_chats()
        self.urls = []

        self.db = defaultdict(dict)

        db_path = Path('./db.txt')
        if db_path.exists() and db_path.stat().st_size != 0:
            with open('./db.txt') as json_file:
                for k, v in json.load(json_file).items():
                    self.db[k] = v

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=selenium")
        self.driver = webdriver.Chrome('./chromedriver_mac', options=chrome_options)
        self.driver.get('https://web.whatsapp.com/')

        try:
            # TODO: This works but is a bit hacky, waiting for ID app doesn't work though
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.ID, "Layer_1")))

        except:
            print("Too Slow :(")

    def quit(self):
        self.driver.quit()

    def grab_group_chats(self):
        return self.driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "_25Ooe", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')

    def grab_urls_from_threads(self):

        urls = []

        for i in range(len(self.grab_group_chats())):
            # We need to re-grab the group chat elements every time because scrolling changes the DOM Tree
            group_chat_elements = self.grab_group_chats()
            group_chat = group_chat_elements[i]
            group_chat.click()

            group_chat_name_elem = self.driver.find_element_by_xpath('//*[(@id = "main")]//*[contains(concat( " ", @class, " " ), concat( " ", "_1wjpf", " " ))]')
            group_chat_name = group_chat_name_elem.text

            # TODO: Implement code that scrolls until the top or until we've seen it before
            time.sleep(2)
            for _ in range(5):
                self.driver.execute_script("document.getElementsByClassName('copyable-area')[0].lastChild.scrollBy(0,-500)")

            chat_bubble_elems = self.driver.find_elements(By.XPATH,
                                                '//*[contains(concat( " ", @class, " " ), concat( " ", "copyable-text", " " ))]')

            for chat_bubble in chat_bubble_elems:

                message_urls = []
                for link in chat_bubble.find_elements_by_xpath('.//a'):
                    url = link.get_attribute('href')
                    if url not in urls:
                        message_urls.append(url)

                timestamp = chat_bubble.get_attribute('data-pre-plain-text')
                if timestamp is not None:
                    timestamp = timestamp.split(" ")[:-3]
                    timestamp = " ".join(timestamp)

                if len(message_urls) != 0:
                    self.urls.extend(message_urls)

                    # Save into DB
                    if timestamp is not None and \
                            (group_chat_name not in self.db or timestamp not in self.db[group_chat_name]):
                        self.db[group_chat_name][timestamp] = message_urls

        # TODO: Print a summary

    def url_counts(self):
        counts = Counter()
        for url in self.urls:
            counts[url] += 1

        with open("url_counts.txt", 'w') as f:
            for k, v in counts.most_common():
                f.write("{}, {}\n".format(v, k))

        with open('db.txt', 'w') as outfile:
            json.dump(self.db, outfile)


if __name__ == "__main__":
    scraper = WhatsAppScraper()
    scraper.grab_group_chats()
    scraper.grab_urls_from_threads()
    scraper.url_counts()
    scraper.quit()




