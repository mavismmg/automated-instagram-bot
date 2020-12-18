#Copyright 2020, Mateus Jorge - suminz9, All rights reserved.

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
                # Attach all ranged hrefs to an array
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(Value)
                href_in_range = browser.find_elements_by_tag_name('a')
                href_in_range = [elem.get_attribute('href') for elem in href_in_range if '.com/p/' in elem.get_attribute('href')]

                [image_hrefs.append(href) for href in href_in_range if href not in image_hrefs]

                print(hashtag + ' images: ' + str(len(image_hrefs)))

            except Exception: continue

        likeable_image = len(image_hrefs)
        swap = 0

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
                    swap = swap + notConst

                    if swap == valueConst:
                        print("Swap")

                        # Get into random user profile
                        # Beggining of the Swap script
                        # getUserProfile(browser)
                        profile = browser.find_elements_by_tag_name('a').click() # Temporary
                        profile().click()

                        p_image_hrefs = []
                        for i in range(1, 14):
                            # Attach all ranged hrefs to an array
                            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                            time.sleep(3)
                            profile_href_in_range = browser.find_elements_by_tag_name('a')
                            profile_href_in_range = [p_elem.get_attribute('href') for p_elem in profile_href_in_range if '.com/p/' in p_elem.get_attribute('href')]

                            [p_image_hrefs.append(href) for href in href_in_range if href not in p_image_hrefs]

                            print(hashtag + ' profile images: ' +str(len(p_image_hrefs)))

                            p_countValue, p_flagValue , p_notConst = randomGenerator()
                            p_images, t_images = randomLikeGenerator()
                            # random_pcountValue_generator = random.randint(1, 3)
                            # random_pflagValue_generator = random.randint(1, 3)

                            if p_countValue == p_flagValue:
                                print("Profile Sleeping and Swaping script:") # Temporary
                                break

                                # time.sleep(random.randint(12, 25))
                                # p_profile = getUserProfile(browser)
                                # p_profile.click()
                                #
                                # # Create a function to do other stuff with the bot using the p_profile variable which
                                # # return the state of the profiel
                                #
                                # followUser()
                                # getHome()
                                # getHashtag(browser, flag)

                            else:
                                like_pimages = lambda: browser.find_elements_by_css_selector('[aria-label="Like"')[p_images].click()
                                like_pimages().click()

                            time.sleep(random.randint(12, 25))
                            p_profile = getUserProfile(browser)
                            p_profile.click()

                            # Create a function to do other stuff with the bot using the p_profile variable which
                            # return the state of the profiel

                            userFollow = browser.find_elements_by_xpath("//button[text()='Follow']").click()
                            userFollow().click()
                            time.sleep(Value)

                            resetPage = browser.find_elements_by_css_selector("[aria-label='Home']").click()
                            resetPage().click()
                            time.sleep(Value)

                            new_tag = getHashtag() # Temporary
                            browser.get('https://www.instagram.com/explore/tags/' + new_tag + '/')
                            time.sleep(Value)

                            # followUser()
                            # getHome()
                            # getHashtag(browser, flag)

                else:
                    like_button = lambda: browser.find_elements_by_css_selector('[aria-label="Like"]')[t_images].click()
                    like_button().click()

                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + " count " + str(second))
                    time.sleep(1)

            except Exception as e: time.sleep(2)
            likeable_image -= 1

def getUserProfile(self):
    browser = self.browser
    # Return the element of the profile
    return browser.find_elements_by_tag_name('a').click()

def getHome(self):
    browser = self.browser
    browser.find_elements_by_css_selector("[aria-label='Home']").click()
    time.sleep(Value)

def getHashtag(browser, flag):
    ObjHashtag = open("HASHTAGS.txt", "r")

    # Verify if it's the first time that the script is running
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
    # Generate random parameters
    parameterValue = random.randint(1, 5)
    flagValue = random.randint(1, 5)
    notConst = random.randint(1, 2)
    notConst = notConst / 2

    return parameterValue, flagValue, notConst

def randomLikeGenerator():
    profile_images = random.randint(0, 6)
    tag_images =  random.randint(0, 12)

    return profile_images, tag_images

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