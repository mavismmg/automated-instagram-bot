# Copyright 2020, Mateus Jorge - suminz9, All rights reserved.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random
import engine
import constantes
import dbusers
import matplotlib.pyplot as plt


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


def login(browser, hashtag):
    HomePage(browser)
    time.sleep(5)
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(constantes.INST_USER)
    password_input.send_keys(constantes.INST_PASS)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    time.sleep(5)
    Script(browser, hashtag)


def Script(browser, hashtag):
    # Mudar toda a class para function
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
    count = 0
    # Inicio do Script
    for image_href in image_hrefs:
        # Começa a percorrer todas as imagens armazenadas no vetor image_hrefs
        browser.get(image_href)
        geturl = browser.current_url
        profile_name = browser.find_element_by_xpath(
            '/html/body/div/section/main/div/div/article/header/div[2]/div/div/span/a').text
        print("{}".format(profile_name))
        time.sleep(3)
        countvalue, flagvalue = randomGenerator()

        print("{}".format('Começando execução da primeira Tarefa'))
        time.sleep(random.randint(2, 4))

        if countvalue == constantes.VALUECONST:
            print("{}".format('Sleeping'))
            timedOut()
            swap += 1
            if swap == constantes.VALUECONST:
                print("{}".format('Swapping'))
                swap = 0
                Script_User(browser, profile_name)
                break

        else:
            like = browser.find_element_by_css_selector('[aria-label="Curtir"]')
            like_limit = browser.find_element_by_xpath(
                '/html/body/div/section/main/div/div/article/div[3]/section[2]/div/div[2]/button/span').text
            integer = int(like_limit)
            print('Quantida de curtidas da imagem {}'.format(integer))
            if integer > constantes.LIKES_LIMIT:
                print("{}".format('Não curtido'))
            else:
                count += 1
                print("Imagem curtida, total {}".format(count))
                like.click()

            print("Perfil de {0}".format(profile_name))
            if profile_name not in previous_user_list:
                if browser.find_element_by_xpath('//button[text()="Seguir"]'):
                    dbusers.add_user((profile_name))
                    browser.find_element_by_xpath('//button[text()="Seguir"]').click()
                    followed += 1
                    print("Seguidos: {0}, #{1}".format(profile_name, followed))
                    new_followers.append((profile_name))
                elif browser.find_element_by_xpath('//button[text()="Seguindo"]'):
                    continue
                else:
                    continue
            else:
                like.click()
                like.sendkeys(Keys.ENTER)
                like_comment = browser.find_elements_by_css_selector('[aria-label="Curtir"]')[random.randint(0, 5)]
                like_comment().click()
                likes += 1
                if likes > 12:
                    print("{}".format('Colocando o bot para dormir ou realizar outras tarefas'))
                    browser.find_element_by_css_selector('[aria-label="Adicione um comentário...').click()
                    browser.sendkeys('Muito bom!')
                    # Criar algo para o bot realizar

                time.sleep(random.randint(5, 18))


    likeable_image -= 1

    for l in range(0, len(new_followers)):
        previous_user_list.append(new_followers[l])

        print("Curtidas {} fotos.".format(likes))
        print("Seguidos {} novas pessoas.".format(followed))


def Script_User(browser, user):
    random_profile_choice = []
    for perfil in user:
        random_profile_choice = perfil

    random_profile_choice = random.choice(perfil)
    browser.get('https://www.instagram.com/' + random_profile_choice + '/')
    time.sleep(5)
    user_hrefs = getAttributesScript(browser, user)
    previous_user_href = dbusers.get_previous_hrefs()
    new_hrefs = []
    count = 0

    for user_href in user_hrefs:
        browser.get(user_href)
        # Não analisar mesma foto varias vezes, otmizar processo
        if user_href not in previous_user_href:
            dbusers.add_href(user_href)
            try:
                like_limit = browser.find_element_by_xpath(
                    '/html/body/div/section/main/div/div/article/div[3]/section[2]/div/div[2]/button/span').text
                integer = int(like_limit)
                print('Quantida de curtidas da imagem {}'.format(integer))
                like = browser.find_element_by_css_selector('[aria-label="Curtir"]')
                if integer > constantes.LIKES_LIMIT:
                    print('{}'.format('Excesso de curtidas'))
                    # Não curtir fotos com muitas curtidas
                else:
                    count += 1
                    print('Imagem curtida, total {}'.format(count))
                    like.click()

            except Exception:
                time.sleep(2)
        else:
            continue


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


def messages(value):
    messages = ["Swap", "Sleeping", "Sleeping and Swapping the Bot Script"]
    print(messages[value])


def timedOut():
    time_out = []
    time_sleep = time.sleep(random.randint(18, 360))
    print('Tempo dormindo {}'.format(time_sleep))

    for second in reversed(range(0, random.randint(18, 28))):
        print('Waking up in {}'.format(second))
        time.sleep(1)

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
    ObjHashtag = constantes.HASHTAGS

    if flag == constantes.FLAG:
        browser.find_element_by_xpath("//span[text()='Pesquisar']")
        tag = browser.sendkeys("#" + random.choice(ObjHashtag))
        browser.sendkeys(Keys.ENTER)
        time.sleep(3)
    else:
        tag = random.choice(ObjHashtag)

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
    flag = 0
    browser = webdriver.Firefox()

    tag = getHashtag(browser, flag)

    engine.init(browser, tag)
    engine.update(browser)


if __name__ == '__main__':
    main()
