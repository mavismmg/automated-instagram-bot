from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

class InstagramLogin:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    def Login(self, hashtag):
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
        swap_flagRange = 0
        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)
            random_countValue_generator = random.randint(1, 5)
            random_flagValue_generator = random.randint(1, 5)
            not_valueConst = random.randint(1, 2)
            not_valueConst = not_valueConst/2
            valueConst = 4

            try:
                time.sleep(random.randint(2, 4))

                if random_countValue_generator == random_flagValue_generator:
                    print("Sleeping")

                    time.sleep(random.randint(18, 360))
                    swap_flagRange = swap_flagRange + not_valueConst

                    if swap_flagRange == valueConst:
                        print("Swap")
                        getUser_profile = browser.find_elements_by_tag_name('a')
                        getUser_profile.click()

                        p_image_hrefs = []
                        for i in range(1, 14):
                            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                            time.sleep(3)
                            profile_href_in_range = browser.find_elements_by_tag_name('a')
                            profile_href_in_range = [p_elem.get_attribute('href') for p_elem in profile_href_in_range if '.com/p/' in p_elem.get_attribute('href')]

                            [p_image_hrefs.append(href) for href in href_in_range if href not in p_image_hrefs]

                            print(hashtag + ' profile images: ' +str(len(p_image_hrefs)))

                            random_pcountValue_generator = random.randint(1, 3)
                            random_pflagValue_generator = random.randint(1, 3)

                            # Organize in functions
                            if random_pcountValue_generator == random_pflagValue_generator:
                                print("Profile Sleeping:")
                                time.sleep(random.randint(12, 25))
                                getUser_profile = browser.find_elements_by_tag_name('a')
                                getUser_profile.click()
                                time.sleep(3)
                                user_follow = browser.find_elements_by_xpath("//button[text()='Follow']")
                                user_follow.click()
                                time.sleep(3)
                                getHome_feed = browser.find_elements_by_css_selector('[aria-label="Home"]')
                                getHome_feed.click()
                                time.sleep(3)
                                search_hashtag = browser.find_elements_by_xpath("//span[text()='Search']")
                                search_hashtag.sendkeys('#' + random.choice(hashtag))
                                search_hashtag.sendkeys(Keys.ENTER)
                                time.sleep(3)
                            else:
                                like_pimages = lambda: browser.find_elements_by_css_selector('[aria-label="Like"')[random.randint(0, 6)].click()
                                like_pimages().click()

                else:
                    like_button = lambda: browser.find_elements_by_css_selector('[aria-label="Like"]')[random.randint(0, 12)].click()
                    like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + " count " + str(second))
                    time.sleep(1)

            except Exception as e: time.sleep(2)
            likeable_image -= 1

def Main():
    ObjUser = open("USERNAME.txt", "r")
    ObjPassword = open("PASSWORD.txt", "r")
    ObjHashtag = open("HASHTAGS.txt", "r")

    insta_user = InstagramLogin(webdriver.Firefox(), ObjUser.read(), ObjPassword.read())
    tag = random.choice(ObjHashtag.readlines())
    insta_user.Login(tag)

if __name__ == '__main__':
    Main()