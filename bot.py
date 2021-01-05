# Copyright 2020, Mateus Jorge - suminz9, All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import engine
import constantes
import dbusers
import matplotlib.pyplot as plt


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


# class FollowUser:
#     def __init__(self, browser):
#         self.browser = browser
#         user_profile = self.browser.find_element_by_tag_name('a')
#         user_profile.click()
#         time.sleep(5)
#         try:
#             username_follow = self.browser.find_element_by_xpath("//button[text()='Seguir']")
#             username_follow.click()
#         except:
#             self.browser.find_element_by_xpath("//button[text()='Enviar mensagem']")
#
#         time.sleep(3)
#         geturl = self.browser.current_url
#         profile_name = geturl.split("/")
#         print(profile_name[3])
#         profile = getAttributesScript(browser, profile_name[3])  # Indexated
#         profile_likeable = len(profile)
#         # for profiles in profile:
#         #     browser.get(profiles)
#         #     time.sleep(3)
#         #     try:
#         #         time.sleep(random.randint(2, 4))
#         #         LikeImage(browser)
#         #     except Exception as e:
#         #         time.sleep(2)
#         #
#         # profile_likeable -= 1


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
        # Redirecionar para página inicial
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        # Chamada da funcao para pegar os href das imagens
        image_hrefs = getAttributesScript(browser, hashtag)
        # Variaveis
        flag = constantes.FLAG
        likeable_image = len(image_hrefs)
        swap = 0
        previous_user_list = dbusers.get_followed_users()
        new_followers = []
        followed = 0
        likes = 0
        # Inicio do Script
        for image_href in image_hrefs:
            # Começa a percorrer todas as imagens armazenadas no vetor image_hrefs
            browser.get(image_href)
            geturl = self.browser.current_url
            profile_name = browser.find_element_by_xpath(
                '/html/body/div/section/main/div/div/article/header/div[2]/div/div/span/a').text
            print("{}".format(profile_name))
            time.sleep(3)
            countvalue, flagvalue = randomGenerator()
            try:
                time.sleep(random.randint(2, 4))
                if countvalue == constantes.VALUECONST:
                    print("{}".format('Sleeping'))
                    timedOut()
                    swap += 1
                    if swap == constantes.VALUECONST:
                        print("{}".format('Swapping'))
                        swap = 0
                        for i in range(1, 14):
                            print("Criar função")
                            # Mudar para perfil do usuario.

                else:
                    like = browser.find_element_by_css_selector('[aria-label="Curtir"]')
                    if like > constantes.LIKES_LIMIT:
                        print("Curtidas restantes {0}".format(profile_name))
                        likes_over_limit = True

                    like.click()
                    print("Perfil de {0}".format(profile_name))
                    if profile_name not in previous_user_list:
                        if browser.find_element_by_xpath('//button[text()="Seguir"]'):
                            dbusers.add_user((profile_name))
                            browser.find_element_by_xpath('//button[text()="Seguir"]').click()
                            followed += 1
                            print("Seguidos: {0}, #{1}".format(profile_name, followed))
                            new_followers.append((profile_name))

                    like_comment = browser.find_elements_by_css_selector('[aria-label="Curtir"]')[random.randint(1, 5)]
                    like_comment().click()
                    likes += 1
                    time.sleep(random.randint(5, 18))

            except Exception as e: time.sleep(2)

        likeable_image -= 1

        for l in range(0, len(new_followers)):
            previous_user_list.append(new_followers[l])

            print("Curtidas {} fotos.".format(likes))
            print("Seguidos {} novas pessoas.".format(followed))

        # previous_user_list = dbusers.get_followed_users()
        # new_followers = []
        # followed = 0
        # likes = 0



        # image_hrefs_follow = []
        # for i in range(1, 7):
        #     try:
        #         browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #         time.sleep(3)
        #         href_in_range = browser.find_elements_by_tag_name('a')
        #         href_in_range = [elem.get_attribute('href') for elem in href_in_range if
        #                          '.com/p/' in elem.get_attribute('href')]
        #
        #         [image_hrefs_follow.append(href) for href in href_in_range if href not in image_hrefs_follow]
        #
        #         print(hashtag + ' images: ' + str(len(image_hrefs_follow)))
        #
        #         #random.choice(image_hrefs)
        #
        #         #FollowUser(browser)
        #     except Exception:
        #         continue
        #
        #     likeable_image -= 1

        previous_user_list = dbusers.get_followed_users()
        new_followers = []
        followed = 0
        likes = 0
        # for hashtag in constantes.HASHTAGS:
        #     browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        #     time.sleep(3)
        #     first_href = browser.find_element_by_xpath(
        #         '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        #     first_href.click()
        #     time.sleep(random.randint(3, 5))
        #     try:
        #         for i in range(1, 200):
        #             start_date = datetime.datetime.now()
        #             profile_name = browser.find_element_by_xpath(
        #                 '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
        #             likes_over_limit = False
        #             print("Estou Aqui")
        #             try:
        #                 like = browser.find_element_by_css_selector('[aria-label="Curtir"]')
        #                 # if like > constantes.LIKES_LIMIT:
        #                 #     print("Curtidas restantes {0}".format(profile_name))
        #                 #     likes_over_limit = True
        #                 like.click()
        #                 print("Perfil de: {0}".format(profile_name))
        #                 if profile_name not in previous_user_list:
        #                     if browser.find_element_by_xpath('//button[text()="Seguir"]'):
        #                         dbusers.add_user(profile_name)
        #                         browser.find_element_by_xpath('//button[text()="Seguir"]').click()
        #                         followed += 1
        #                         print("Seguidos: {0}, #{1}".format(profile_name, followed))
        #                         new_followers.append((profile_name))
        #
        #                     browser.find_element_by_css_selector('[aria-label="Curtir"]').click()
        #                     likes += 1
        #                     print("Curtidas {0}'s post, #{1}".format(profile_name, likes))
        #                     time.sleep(random.randint(5, 18))
        #
        #                 browser.find_element_by_link_text('Próximo').click()
        #                 time.sleep(10, 30)
        #
        #             except: continue
        #
        #             end_date = datetime.datetime.now()
        #             time_elapsed = end_date - start_date
        #             print("Tempo decorrido: {0} segundos".format(time_elapsed.total_seconds()))
        #
        #     except: continue
        #
        #     for l in range(0, len(new_followers)):
        #         previous_user_list.append(new_followers[l])
        #         print("Curtidas {} fotos.".format(likes))
        #         print("Seguidos {} novas pessoas.".format(followed))

        # for hashtag in constantes.HASHTAGS:
        #     browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        #     time.sleep(3)
        #     first_href = browser.find_element_by_xpath(
        # '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        #     first_href.click()
        #     time.sleep(random.randint(1, 3))
        #     try:
        #         for i in range(1, 200):
        #             start = datetime.datetime.now()
        #             geturl = self.browser.current_url
        #             profile_name = geturl.split("/")
        #             likes_over_limit = False
        #             try:
        #                 likes = int(browser.find_element_by_css_selector('[aria-label="Curtir"]'))
        #                 if likes > constantes.LIKES_LIMIT:
        #                     print("Curtidas restantes {0}".format(profile_name))
        #                     likes_over_limit = True
        #
        #                 print("Perfil de: {0}".format(profile_name))
        #                 if profile_name not in previous_user_list and not likes_over_limit:
        #                     if browser.find_element_by_xpath("//button[text()='Seguir']"):
        #                         dbusers.add_user(profile_name)
        #                         browser.find_element_by_xpath("//button[text()='Seguir']").click()
        #                         followed += 1
        #                         print("Seguidos: {0}, #{1}".format(profile_name, followed))
        #                         new_followers.append(profile_name)
        #
        #                     image_like = self.browser.find_element_by_css_selector('[aria-label="Curtir"]')
        #                     image_like.click()
        #                     likes += 1
        #                     print("Curtidas {0}'s post, #{1}".format(profile_name, likes))
        #                     time.sleep(random.randint(5, 18))
        #
        #                 browser.find_element_by_link_text('Proximo').click()
        #                 time.sleep(random.randint(20, 30))
        #
        #             except:
        #                 continue
        #
        #             end = datetime.datetime.now()
        #             time_elapsed = end - start
        #             print("Tempo decorrido: {0} segundos".format(time_elapsed.total_seconds()))
        #
        #     except:
        #         continue
        #
        #         #  Add new list to old list
        #     for l in range(0, len(new_followers)):
        #         previous_user_list.append(new_followers[l])
        #
        #         print("Curtidas {} fotos.".format(likes))
        #         print("Seguidos {} novas pessoas.".format(followed))
        #     # browser.get(image_href_follow)
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
    time_out = []
    time_out = time.sleep(random.randint(18, 360))

    time.sleep(time_out)

    after_flag = 0
    flag_max = 5

    if after_flag == flag_max:
        plt.title("TimeOut Timings")
        plt.xlabel("Axys X")
        plt.ylabel("Axys Y")
        plt.plot(time_out, color='k')
        plt.show()
    else:
        after_flag += 1


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
    # Att: Resolvido

    if flag == constantes.FLAG:
        browser.find_element_by_xpath("//span[text()='Pesquisar']")
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


def unfollow_people(browser, user):
    if not isinstance(user, (list, )):
        u = user
        user = []
        user.append(u)

    for perfil in user:
        try:
            browser.get('https://www.instagram.com/' + perfil + '/')
            time.sleep(5)
            unfollow_xpath = browser.find_element_by_xpath('[aria-label="Seguindo"]')
            unfollow_confirm_xpath = \
                '/html/body/div/section/main/div/header/section/div/div/div/div[2]/div/span/span/button/div/span'

            if browser.find_element_by_xpath(unfollow_xpath).text == 'Seguindo':
                time.sleep(random.randint(5, 20))
                browser.find_element_by_xpath(unfollow_xpath).click()
                time.sleep(3)
                browser.find_element_by_xpath(unfollow_confirm_xpath).click()
                time.sleep(3)

            dbusers.delete_user(perfil)

        except Exception: continue


def main():
    flag = 0
    browser = webdriver.Firefox()

    tag = getHashtag(browser, flag)

    engine.init(browser, tag, flag)
    engine.update(browser)

    #insta_user = InstagramLogin(browser, objUser.read(), objPassword.read())

    #insta_user.login(tag, flag)


if __name__ == '__main__':
    main()
