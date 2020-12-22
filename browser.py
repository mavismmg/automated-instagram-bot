#Copyright 2020, Mateus Jorge - suminz9, All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

# Global Variables
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

class FollowUser:
    def __init__(self, browser):
        self.browser = browser
        username_follow = self.browser.find_elements_by_xpath("//button[text()='Follow']")
        username_follow.click()
        time.sleep(2)

class LikeImage:
    def __init__(self, browser):
        self.browser = browser
        image_like = lambda: self.browser.find_elements_by_css_selector('[aria-label="Like"]')[random.randint(0,  8)].click()
        image_like().click()
        time.sleep(2)

class ActivityFeed:
    def __init__(self, browser):
        self.browser = browser
        activity_feed = self.browser.find_elements_by_css_selector("[aria-label='Activity Feed']")
        activity_feed.click()
        time.sleep(3)

# Change, make it clean by creating a LikeUser class
class Script:
    def __init__(self, browser, hashtag, flag):
        self.browser = browser
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        flag = Flag

        image_hrefs = getAttributesScript(browser, hashtag)

            # image_hrefs = []
            # for i in range(1, 7):
            #     try:
            #         # Attach all ranged hrefs to an array
            #         browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            #         time.sleep(Value)
            #         href_in_range = browser.find_elements_by_tag_name('a')
            #         href_in_range = [elem.get_attribute('href') for elem in href_in_range if '.com/p/' in elem.get_attribute('href')]
            #
            #         [image_hrefs.append(href) for href in href_in_range if href not in image_hrefs]
            #
            #         print(hashtag + ' images: ' + str(len(image_hrefs)))
            #
            #     except Exception: continue

        likeable_image = len(image_hrefs)
        Swap = 0

        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)

            countValue, flagValue = randomGenerator()
            valueConst = 4

            try:
                time.sleep(random.randint(2, 4))
                profile_image = randomLikeGenerator()
                print(profile_image) # Temporary

                if countValue == flagValue:
                    print("Sleeping") # Temporary

                    timedOut()

                    Swap = Swap + 1

                    if Swap == valueConst:
                        print("Swap")

                        # Get into random user profile
                        # Beginning of the Swap script
                        # getUserProfile(browser)

                        for i in range(1, 14):
                            # Attach all ranged hrefs to an array
                            profile_image_hrefs = getAttributesScript(browser, hashtag)

                                # browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                                # time.sleep(3)
                                # profile_href_in_range = browser.find_elements_by_tag_name('a')
                                # profile_href_in_range = [p_elem.get_attribute('href') for p_elem in profile_href_in_range if '.com/p/' in p_elem.get_attribute('href')]
                                #
                                # [p_image_hrefs.append(href) for href in href_in_range if href not in p_image_hrefs]
                                #
                                # print(hashtag + ' profile images: ' +str(len(p_image_hrefs)))

                            profile_countValue, profile_flagValue , profile_notConst = randomGenerator()
                            profile_images, tag_images = randomLikeGenerator()

                            print(profile_countValue, profile_flagValue, profile_notConst) # Temporary
                            print(profile_images, tag_images) # Temporary

                            if profile_countValue == profile_flagValue:
                                print("Profile Sleeping and Swaping script:") # Temporary

                                HomePage(browser) # Get back into homepage
                                ActivityFeed(browser) # Make the bot check if someone followed him

                            else:
                                FollowUser(browser)
                                    # userFollow = browser.find_elements_by_xpath("//button[text()='Follow']").click()  # Temporary
                                    # userFollow().click()
                                    # time.sleep(Value)

                                LikeImage(browser)
                                    # like_pimages = lambda: browser.find_elements_by_css_selector('[aria-label="Like"]')[
                                    #     random.randint(0, 8)].click()
                                    # like_pimages().click()

                            time.sleep(random.randint(12, 25))
                            # p_profile = getUserProfile(browser) Need to be fixed
                            # p_profile.click()

                            # Create a function to do other stuff with the bot using the p_profile variable which
                            # return the state of the profiel


                            # resetPage = browser.find_elements_by_css_selector("[aria-label='Home']").click()
                            # resetPage().click()
                            # time.sleep(Value)
                            #
                            # new_tag = getHashtag() # Temporary
                            # browser.get('https://www.instagram.com/explore/tags/' + new_tag + '/')
                            # time.sleep(Value)

                            # followUser()
                            # getHome()
                            # getHashtag(browser, flag)
                else:
                    LikeImage(browser)
                        # like_button = lambda: browser.find_elements_by_css_selector('[aria-label="Like"]')[random.randint(0, 6)].click()
                        # like_button().click()
                    FollowUser(browser)
                        # userFollow = browser.find_elements_by_xpath("//button[text()='Follow']").click()  # Temporary
                        # userFollow().click()

                timedOutCounter(hashtag)
                    # for second in reversed(range(0, random.randint(18, 28))):
                    #     print("#" + hashtag + " count " + str(second))
                    #     time.sleep(1)

            except Exception as e: time.sleep(2)
            likeable_image -= 1

# def getUserProfile(self):
#     browser = self.browser
#     # Return the element of the profile
#     return browser.find_elements_by_tag_name('a').click()
#
# def getHome(self):
#     browser = self.browser
#     browser.find_elements_by_css_selector("[aria-label='Home']").click()
#     time.sleep(Value)

def timedOut():
    time.sleep(random.randint(18, 360))

def timedOutCounter(hashtag):
    for second in reversed(range(0, random.randint(18, 28))):
        print("#" + hashtag + " count " + str(second))
        time.sleep(1)

def getAttributesScript(browser, hashtag):
    image_hrefs = []

    for i in range(1, 7):
        try:
            # Attach all ranged hrefs to an array
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
            href_in_range = browser.find_elements_by_tag_name('a')
            href_in_range = [elem.get_attribute('href') for elem in href_in_range if
                             '.com/p/' in elem.get_attribute('href')]

            [image_hrefs.append(href) for href in href_in_range if href not in image_hrefs]

            print(hashtag + ' images: ' + str(len(image_hrefs)))

        except Exception:
            continue

    return image_hrefs

def getHashtag(browser, flag):
    ObjHashtag = open("HASHTAGS.txt", "r")

    # Verify if it's the first time that the script is running
    if flag == Flag:
        browser.find_element_by_xpath("//span[text()='Search']")
        tag = browser.sendkeys("#" + random.choice(ObjHashtag.readlines()))
        browser.sendkeys(Keys.ENTER)
        time.sleep(3)
    else:
        tag = random.choice(ObjHashtag.readlines())

    return tag

# def followUser(self):
#     browser = self.browser
#     browser.find_element_by_xpath("//button[text()='Follow']").click()
#     time.sleep(Value)

def randomGenerator():
    # Generate random parameters
    parameterValue = random.randint(1, 5)
    flagValue = random.randint(1, 5)

    return parameterValue, flagValue

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