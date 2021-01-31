from selenium import webdriver
import time
import urllib.request
import os


class Scraper(object):
    def __init__(self, headless=True):
        self.driver_path = '/Users/tommasoscarlatti/chromedriver'
        self.headless = headless

        # Use headless browser
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            self.driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        else:
            self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def update_and_download(self, gamertag="tmscarla"):
        self.driver.get("https://codstats.net/warzone/profile/xbox/" + gamertag)
        time.sleep(3)

        # Click on update stats button
        main_div = self.driver.find_element_by_class_name("main_content")
        divs = main_div.find_elements_by_tag_name("div")

        for div in divs:
            if div.text == "Update Stats":
                div.click()
                break

        # Wait 15s
        print('Updating...')
        time.sleep(15)

        # Download image
        print('Downloading...')
        self.driver.get("http://codstats.net/warzone/card.jpg?name=" + gamertag + "&pl=3&mode=16")
        src = self.driver.find_element_by_tag_name("img").get_attribute("src")
        urllib.request.urlretrieve(src, "../img/cod_card.jpg")
        print('Done.')


if __name__ == '__main__':
    GAMERTAG = "tmscarla"

    scraper = Scraper()
    scraper.update_and_download(gamertag=GAMERTAG)
