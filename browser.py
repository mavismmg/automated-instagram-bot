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
        InstaScript(browser, hashtag)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

class InstaScript:
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

        like_flag = 5
        like_count = 0
        likeable_image = len(image_hrefs)
        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)
            like_count = like_count + 1
            try:
                time.sleep(random.randint(2, 4))
                if (like_count == like_flag):
                    print("Sleeping ...")
                    time.sleep(random.randint(18, 360))
                    like_count = 0
                else:
                    like_button = lambda: browser.find_elements_by_css_selector('[aria-label="Like"]')[random.randint(0, 12)].click()
                    like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + " | Sleeping " + str(second))
                    time.sleep(1)

            except Exception as e: time.sleep(2)
            likeable_image -= 1

        follow_user = len(image_hrefs)
        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)

            follow_button = lambda : browser.find_elements_by_css_selector("button")[random.randint(5, 10)].click()
            follow_button().click()


#Temporary
insta_user = InstagramLogin(webdriver.Firefox(), "username", "password")
hashtags = ['bike', 'bikes', 'cars']
tag = random.choice(hashtags)
insta_user.login(tag)
