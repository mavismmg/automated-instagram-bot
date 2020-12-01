from selenium import webdriver

import time

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
        for i in range(1, 3):
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)

        hrefs = browser.find_elements_by_tag_name('a')
        image_hrefs = [elem.get_attribute['href'] for elem in hrefs]
        image_hrefs = [href for href in image_hrefs if hashtag in href]
        print(hashtag + 'images:' + str(len(image_hrefs)))

insta_user = InstagramLogin(webdriver.Firefox(), "username", "passworld")
insta_user.login("cars")