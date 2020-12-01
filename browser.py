from selenium import webdriver

import time
import random

class InstagramLogin:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    def login(self, hashtag):
        browser = self.browser
        HomePage(browser)
        time.sleep(5)
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(5)
        InstaLikes(browser, hashtag)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

class InstaLikes:
    def __init__(self, browser, hashtag):
        self.browser = browser
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)

        #Temporary implementation - outdated
        image_hrefs = []
        for i in range(1, 7):
            try:
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                href_in_range = browser.find_elements_by_tag_name('a')
                href_in_range = [elem.get_attribute('href') for elem in href_in_range if '.com/p/' in elem.get_attribute('href')]

                [image_hrefs.append(href) for href in href_in_range if href not in image_hrefs]

                print(hashtag + ' images: ' + str(len(image_hrefs)))

            except Exception: continue

        likeable_image = len(image_hrefs)
        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: browser.find_elements_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': likeable images left: ' + str(likeable_image) + "  | Sleeping " + str(second))
                    time.sleep(3)

            except Exception as e: time.sleep(3)
            likeable_image -= 1

#Temporary
insta_user = InstagramLogin(webdriver.Firefox(), "username", "password")
insta_user.login("hashtag")