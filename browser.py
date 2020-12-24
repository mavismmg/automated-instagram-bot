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
        user_profile = self.browser.find_elements_by_tag_name('a')[random.randint(0, 6)].click()
        user_profile().click()
        time.sleep(3)
        username_follow = self.browser.find_elements_by_xpath("//button[text()='Follow']")[random.randint(0, 2)].click()
        username_follow().click()
        time.sleep(3)
        getUrl = self.browser.url
        profile_name = getUrl.split("/")
        profile = getAttributesScript(browser, profile_name)
        profile_likeable = len(profile)
        for profiles in profile:
            browser.get(profiles)
            time.sleep(3)
            try:
                time.sleep(random.randint(2, 4))
                LikeImage(browser)
            except Exception as e: time.sleep(2)

        profile_likeable -= 1

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

class Script:
    def __init__(self, browser, hashtag, flag):
        self.browser = browser
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        flag = Flag
        image_hrefs = getAttributesScript(browser, hashtag)
        likeable_image = len(image_hrefs)
        for image_href in image_hrefs:
            browser.get(image_href)
            time.sleep(3)
            countValue, flagValue = randomGenerator()
            valueConst = 4
            ScriptChanger = None
            try:
                time.sleep(random.randint(2, 4))
                if countValue == flagValue:
                    print(Messages(1))
                    timedOut()
                    ScriptChanger = Swap()
                    if ScriptChanger == valueConst:
                        print(Messages(0))
                        ScriptChanger = None
                        for i in range(1, 14):
                            # Attach all ranged hrefs to an array
                            profile_image_hrefs = getAttributesScript(browser, hashtag)
                            profile_countValue, profile_flagValue , profile_notConst = randomGenerator()
                            profile_images, tag_images = randomLikeGenerator()
                            # Make an use for profile_image_hrefs
                            print(profile_countValue, profile_flagValue, profile_notConst) # Temporary
                            print(profile_images, tag_images) # Temporary
                            if profile_countValue == profile_flagValue:
                                print(Messages(2))
                                HomePage(browser) # Get back into homepage
                                ActivityFeed(browser) # Make the bot check if someone followed him
                            else:
                                LikeImage(browser)

                            time.sleep(random.randint(12, 25))
                else:
                    LikeImage(browser)

                timedOutCounter(hashtag)

            except Exception as e: time.sleep(2)
            likeable_image -= 1

        for follow_href in image_hrefs:
            browser.get(follow_href)
            time.sleep(3)
            countValue, flagValue = randomGenerator()
            valueConst = 4
            try:
                time.sleep(random.randint(2, 4))
                profile_follow = randomLikeGenerator()
                if countValue == flagValue:
                    print(Messages(1))
                    timedOut()
                    ScriptChanger = Swap()
                    if ScriptChanger == valueConst:
                        print(Messages(0))
                        ScriptChanger = None
                        for i in range(1, 14):
                            # Attach all ranged hrefs to an array
                            profile_image_hrefs = getAttributesScript(browser, hashtag)
                            profile_countValue, profile_flagValue, profile_notConst = randomGenerator()
                            profile_images, tag_images = randomLikeGenerator()
                            # Make an use for prfile_image_hrefs
                            print(profile_countValue, profile_flagValue, profile_notConst)  # Temporary
                            print(profile_images, tag_images)  # Temporary
                            if profile_countValue == profile_flagValue:
                                print(Messages(2))
                                HomePage(browser)  # Get back into homepage
                                ActivityFeed(browser)  # Make the bot check if someone followed him
                            else:
                                FollowUser(browser)

                            time.sleep(random.randint(12, 25))
                else:
                    FollowUser(browser)

                timedOutCounter(hashtag)

            except Exception as e:
                time.sleep(2)
            likeable_image -= 1

def Swap():
    ScriptChanger =+ 1
    return ScriptChanger

def Messages(value):
    messages = ["Swap", "Sleeping", "Sleeping and Swapping the Bot Script"]
    print(messages[value])

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