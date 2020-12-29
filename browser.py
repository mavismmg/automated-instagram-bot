# Copyright 2020, Mateus Jorge - suminz9, All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import csv
import engine
import constantes
import dbusers
import datetime
# Global Variables
Flag = 1


def login(browser, hashtag, flag):
    HomePage(browser)
    time.sleep(5)
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(constantes.INST_USER)
    password_input.send_keys(constantes.INST_PASS)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    time.sleep(5)
    Script(browser, hashtag, flag)


class Functionalities:
    def __init__(self, browser, tag, flag):
        self.browser = browser
        self.tag = tag
        self.flag = flag


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')


class FollowUser:
    def __init__(self, browser):
        self.browser = browser
        user_profile = self.browser.find_element_by_tag_name('a')
        user_profile.click()
        time.sleep(5)
        try:
            username_follow = self.browser.find_element_by_xpath("//button[text()='Seguir']")
            username_follow.click()
        except:
            self.browser.find_element_by_xpath("//button[text()='Enviar mensagem']")

        time.sleep(3)
        geturl = self.browser.current_url
        profile_name = geturl.split("/")
        print(profile_name[3])
        profile = getAttributesScript(browser, profile_name[3])  # Indexated
        profile_likeable = len(profile)
        # for profiles in profile:
        #     browser.get(profiles)
        #     time.sleep(3)
        #     try:
        #         time.sleep(random.randint(2, 4))
        #         LikeImage(browser)
        #     except Exception as e:
        #         time.sleep(2)
        #
        # profile_likeable -= 1


class LikeImage:
    def __init__(self, browser):
        self.browser = browser
        image_like = self.browser.find_elements_by_css_selector('[aria-label="Curtir"]')[random.randint(0,  8)].click()
        image_like().click()
        time.sleep(2)


class ActivityFeed:
    def __init__(self, browser):
        self.browser = browser
        activity_feed = self.browser.find_elements_by_css_selector("[aria-label='Activity Feed']") #  Mudar idioma
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
        swap = 0

        # for image_href in image_hrefs:
        #     browser.get(image_href)
        #     time.sleep(3)
        #     countvalue, flagvalue = randomGenerator()
        #     valueConst = 4
        #     try:
        #         time.sleep(random.randint(2, 4))
        #         if countvalue == flagvalue:
        #             print("Sleeping")
        #             timedOut()
        #             swap = swap + 1 #  Mudar Isso
        #             if swap == valueConst:
        #                 print("Swapping")
        #                 swap = 0
        #                 for i in range(1, 14):
        #                     # Attach all ranged hrefs to an array
        #                     profile_image_hrefs = getAttributesScript(browser, hashtag)
        #                     profile_countValue, profile_flagValue = randomGenerator()
        #                     profile_images, tag_images = randomLikeGenerator()
        #                     # Make an use for profile_image_hrefs
        #                     print(profile_countValue, profile_flagValue)  # Temporary
        #                     print(profile_images, tag_images)  # Temporary
        #
        #                     if profile_countValue == profile_flagValue:
        #                         print("Chaning the Key Script")
        #                         HomePage(browser)  # Get back into homepage
        #                         ActivityFeed(browser)  # Make the bot check if someone followed him
        #
        #                     else:
        #                         LikeImage(browser)
        #
        #                     time.sleep(random.randint(12, 25))
        #
        #         else:
        #             LikeImage(browser)
        #
        #         timedOutCounter(hashtag)
        #
        #     except Exception as e:
        #         time.sleep(2)
        #     # likeable_image -= 1
        previous_user_list = dbusers.get_followed_users()
        new_followers = []
        followed = 0
        likes = 0



        image_hrefs_follow = []
        for i in range(1, 7):
            try:
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                href_in_range = browser.find_elements_by_tag_name('a')
                href_in_range = [elem.get_attribute('href') for elem in href_in_range if
                                 '.com/p/' in elem.get_attribute('href')]

                [image_hrefs_follow.append(href) for href in href_in_range if href not in image_hrefs_follow]

                print(hashtag + ' images: ' + str(len(image_hrefs_follow)))

                #random.choice(image_hrefs)

                #FollowUser(browser)
            except Exception:
                continue

            likeable_image -= 1

        for image_href_follow in image_hrefs_follow:
            for hashtag in constantes.HASHTAGS:
                browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
                time.sleep(3)
                first_href = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
                first_href.click()

                try:
                    for i in range(1, 200):
                        start = datetime.datetime.now()
                        geturl = self.browser.current_url
                        profile_name = geturl.split("/")
                        likes_over_limit = False
                        try:
                            likes = int(browser.find_element_by_css_selector('[aria-label="Curtir"]'))
                            if likes > constantes.LIKES_LIMIT:
                                print("Curtidas restantes {0}".format(profile_name))
                                likes_over_limit = True

                            print("Perfil de: {0}".format(profile_name))
                            if profile_name not in previous_user_list and not likes_over_limit:
                                if browser.find_element_by_xpath("//button[text()='Seguir']"):
                                    dbusers.add_user(profile_name)
                                    browser.find_element_by_xpath("//button[text()='Seguir']").click()
                                    followed += 1
                                    print("Seguidos: {0}, #{1}".format(profile_name, followed))
                                    new_followers.append(profile_name)

                                image_like = self.browser.find_element_by_css_selector('[aria-label="Curtir"]')
                                image_like.click()
                                likes += 1
                                print("Curtidas {0}'s post, #{1}".format(profile_name, likes))
                                time.sleep(random.randint(5, 18))

                            time.sleep(18, 36)

                        except:
                            continue

                        end = datetime.datetime.now()
                        time_elapsed = end - start
                        print("Tempo decorrido: {0} segundos".format(time_elapsed.total_seconds()))

                except:
                    continue

                #  Add new list to old list
                for l in range(0, len(new_followers)):
                    previous_user_list.append(new_followers[l])

                print("Curtidas {} fotos.".format(likes))
                print("Seguidos {} novas pessoas.".format(followed))
            # browser.get(image_href_follow)
            # time.sleep(3)
            # random.choice(image_href_follow)
            # FollowUser(browser)
            # try:
            #     FollowUser(browser)
            # except Exception:
            #     time.sleep(2)

# def Swap():
#     ScriptChanger = ScriptChanger + 1
#     return ScriptChanger


def messages(value):
    messages = ["Swap", "Sleeping", "Sleeping and Swapping the Bot Script"]
    print(messages[value])


def timedOut():
    time_out = time.sleep(random.randint(18, 360))
    fields = ["Time", "Seconds"]
    rows = [["Sleep", time_out]]
    with open('TimeOut', 'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)

    time.sleep(time_out)


def timedOutCounter(hashtag):
    for second in reversed(range(0, random.randint(18, 28))):
        print("#" + hashtag + " Count " + str(second))
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
    # Criar algoritmo para verificar hashtag usada, caso a hashtag já tenha sido utilizada em outra execução,
    # escolher outra
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
    tag_images = random.randint(0, 12)

    return profile_images, tag_images


def main():
    objUser = open("USERNAME.txt", "r")
    objPassword = open("PASSWORD.txt", "r")

    flag = 0
    browser = webdriver.Firefox()

    tag = getHashtag(browser, flag)

    engine.init(browser, tag, flag)
    engine.update(browser)

    #insta_user = InstagramLogin(browser, objUser.read(), objPassword.read())

    #insta_user.login(tag, flag)


if __name__ == '__main__':
    main()
