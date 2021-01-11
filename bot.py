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
    # Verificando usuarios, parar de seguir
    engine.update(browser)
    # Redirecionar para página inicial
    browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
    time.sleep(3)
    # Chamada da funcao para pegar os href das imagens
    image_hrefs = getAttributesScript(browser, hashtag)
    # Variaveis
    flag = constantes.FLAG
    likeable_image = len(image_hrefs)
    previous_user_list = dbusers.get_followed_users()
    previous_user_href = dbusers.get_previous_hrefs()
    new_followers = []
    followed = 0
    likes = 0
    count = 0
    swap = 0
    count_string_verification = 0
    # Inicio do Script
    for image_href in image_hrefs:
        if image_href not in previous_user_href:
            # Começa a percorrer todas as imagens armazenadas no vetor image_hrefs
            browser.get(image_href)
            geturl = browser.current_url
            profile_name = browser.find_element_by_xpath(
                '/html/body/div/section/main/div/div/article/header/div[2]/div/div/span/a').text
            print("{}".format(profile_name))
            time.sleep(3)
            countvalue, flagvalue = randomGenerator()

            print("{}".format('Novo ciclo'))
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
                semaphore = False
                like = browser.find_element_by_css_selector('[aria-label="Curtir"]')
                try:
                    if (browser.find_element_by_xpath(
                        '/html/body/div/section/main/div/div/article/div[3]/section[2]/div/div[2]/button/span')):
                        like_limit = browser.find_element_by_xpath(
                            '/html/body/div/section/main/div/div/article/div[3]/section[2]/div/div[2]/button/span').text
                    else:
                        like_limit = browser.find_element_by_xpath(
                            '/html/body/div/section/main/div/div/article/div[3]/section[2]/div/span/span').text
                except Exception:
                    print("{}".format('Não foi possível localizar nenhum elemento, continuando'))
                    time.sleep(1)

                for i in range(len(like_limit)):
                    if like_limit[i] == '.':
                        aux = float(like_limit)
                        aux = aux * (10 ** (i+2))
                        integer_like_limit = int(aux)
                        print("Valor corrigido {}".format(integer_like_limit))
                        semaphore = True

                if semaphore != True:
                    integer_like_limit = int(like_limit)
                print('Quantida de curtidas da imagem {}'.format(integer_like_limit))
                if integer_like_limit > constantes.LIKES_LIMIT:
                    print("{}".format('Não curtido'))
                else:
                    count += 1
                    print("Imagem curtida, total {}".format(count))
                    choice = [True, False]
                    if random.choice(choice) == True and likes < 10:
                        like.click()
                        likes += 1
                        time.sleep(random.randint(18, 30))
                        if likes > 10:
                            print("Muitas curtidas, {}. Bot timeout.".format(likes))
                            time.sleep(random.randint(500, 800))
                            print("Bot wakeup, após excesso de curtidas {}".format(likes))
                            likes = 0

                print("Perfil de {0}".format(profile_name))
                if profile_name not in previous_user_list:
                    if browser.find_element_by_xpath('//button[text()="Seguir"]'):
                        if random.randint(1, 6) == constantes.VALUECONST:
                            dbusers.add_user((profile_name))
                            browser.find_element_by_xpath('//button[text()="Seguir"]').click()
                            followed += 1
                            print("Seguidos: {0}, #{1}".format(profile_name, followed))
                            new_followers.append((profile_name))
                            time.sleep(random.randint(30, 240))
                        else:
                            time.sleep(3)
                            if likes > 1:
                                print("{}".format('Colocando o bot para dormir ou realizar outras tarefas'))
                                # Salvar imagens para classificador de imagens
                                # selenium.common.exceptions.InvalidSelectorException: Message: Given xpath expression
                                # "/html/body/div[5]/div[2]/div/article/div[2]/div/div/div/div/img/"
                                # is invalid: SyntaxError: The expression is not a legal expression.
                                img = browser.find_element_by_xpath(
                                    '/html/body/div[5]/div[2]/div/article/div[2]/div/div/div/div/img/').text

                                print("Div da imagem: {}".format(img))


                    else:
                        print("{}".format('Perfil já está sendo seguido'))
                        continue
                else:
                    try:
                        if browser.find_element_by_css_selector('[aria-label="Descurtir"]'):
                            browser.find_element_by_css_selector('[aria-label="Descurtir"]').click()
                            like_comment = browser.find_elements_by_css_selector('[aria-label="Curtir"]')[
                                random.randint(0, 8)].click()
                            like_comment().click()
                            likes += 1
                        else:
                            like_comment = browser.find_elements_by_css_selector('[aria-label="Curtir"]')[
                                random.randint(0, 8)].click()
                            like_comment().click()
                            likes += 1

                        if likes > 1:  # Was 12
                            print("{}".format('Colocando o bot para dormir ou realizar outras tarefas'))
                            browser.find_element_by_css_selector('[aria-label="Adicione um comentário...').click()
                            browser.sendkeys('Muito bom!')
                            # Salvar imagens para classificador de imagens
                            try:
                                img = browser.find_element_by_xpath(
                                    '/html/body/div[5]/div[2]/div/article/div[2]/div/div/div/div/img/').get_attribute(
                                    'src')

                                print("{}".format(img))
                                img.click()

                            except Exception:
                                time.sleep(3)
                                continue

                    except Exception:
                        continue

                    time.sleep(random.randint(5, 18))
        else:
            print("{}".format('Imagem repetida, ignorando'))
            continue


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
                    print('{}'.format('Não curtido'))
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
        browser.get('https://www.instagram.com/' + perfil + '/')
        time.sleep(5)
        if browser.find_element_by_css_selector('[aria-label="Seguindo"]'):
            time.sleep(random.randint(5, 20))
            browser.find_element_by_css_selector('[aria-label="Seguindo"]').click()
            time.sleep(3)
            browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            time.sleep(3)

        dbusers.delete_user(perfil)



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
    #engine.update(browser)


if __name__ == '__main__':
    main()
