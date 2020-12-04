#Copyright 2020, Mateus Jorge, All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

# Global Variables

Value = 3
Buffer = 5
Flag = 1

class InstagramLogin:
    def __init__(self, browser, username, password):
        self.browser = browser
        self.username = username
        self.password = password

    def Login(self, hashtag, flag):
        browser = self.browser
        HomePage(browser)
        time.sleep(Buffer)
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(Buffer)
        Script(browser, hashtag, flag)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

class Script:
    def __init__(self, browser, hashtag, flag):
        self.browser = browser
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(Value)
        flag = Flag

        image_hrefs = []
        for i in range(1, 7):
            try:
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(Value)
                href_in_range = browser.find_elements_by_tag_name('a')
                href_in_range = [elem.get_attribute('href') for elem in href_in_range if '.com/p/' in elem.get_attribute('href')]

                [image_hrefs.append(href) for href in href_in_range if href not in image_hrefs]

                print(hashtag + ' images: ' + str(len(image_hrefs)))

            except Exception: continue

        likeable_image = len(image_hrefs)
        swap_flagRange = 0

        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(Value)

            countValue, flagValue , notConst = randomGenerator()
            valueConst = 4

            try:
                time.sleep(random.randint(2, 4))

                if countValue == flagValue:
                    print("Sleeping")

                    time.sleep(random.randint(18, 360))
                    swap_flagRange = swap_flagRange + notConst

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
                                getUserProfile()
                                followUser()
                                getHome()
                                getHashtag(browser, flag)


                                # getUser_profile = browser.find_elements_by_tag_name('a')
                                # getUser_profile.click()
                                # time.sleep(3)
                                # user_follow = browser.find_elements_by_xpath("//button[text()='Follow']")
                                # user_follow.click()
                                # time.sleep(3)
                                # getHome_feed = browser.find_elements_by_css_selector('[aria-label="Home"]')
                                # getHome_feed.click()
                                # time.sleep(3)
                                # search_hashtag = browser.find_elements_by_xpath("//span[text()='Search']")
                                # search_hashtag.sendkeys('#' + random.choice(hashtag))
                                # search_hashtag.sendkeys(Keys.ENTER)
                                # time.sleep(3)
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

def getUserProfile(self):
    browser = self.browser
    browser.find_elements_by_tag_name('a').click()
    time.sleep(Value)

def getHome(self):
    browser = self.browser
    browser.find_elements_by_css_selector("[aria-label='Home']").click()
    time.sleep(Value)

def getHashtag(browser, flag):
    ObjHashtag = open("HASHTAGS.txt", "r")

    if flag == Flag:
        browser.find_element_by_xpath("//span[text()='Search']")
        tag = browser.sendkeys("#" + random.choice(ObjHashtag.readlines()))
        browser.sendkeys(Keys.ENTER)
        time.sleep(Value)
    else:
        tag = random.choice(ObjHashtag.readlines())

    return tag

def followUser(self):
    browser = self.browser
    browser.find_element_by_xpath("//button[text()='Follow']").click()
    time.sleep(Value)

def randomGenerator():
    parameterValue = random.randint(1, 5)
    flagValue = random.randint(1, 5)
    notConst = random.randint(1, 2)
    notConst = notConst / 2

    return parameterValue, flagValue, notConst

def Main():
    ObjUser = open("USERNAME.txt", "r")
    ObjPassword = open("PASSWORD.txt", "r")

    flag = 0
    browser = webdriver.Firefox()

    insta_user = InstagramLogin(browser, ObjUser.read(), ObjPassword.read())
    tag = getHashtag(browser, flag)
    insta_user.Login(tag, flag)

if __name__ == '__main__':
    Main()