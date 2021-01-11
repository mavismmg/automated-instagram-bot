import bot, dbusers
import constantes
import datetime
import time


def init(webdriver, tag):
    constantes.init()
    bot.login(webdriver, tag)


def update(browser):
    start = datetime.datetime.now()
    follow_list_check(browser)
    end = datetime.datetime.now()
    elapsed = end - start

    if elapsed.total_seconds() >= constantes.CHECK_FOLLOWERS_EVERY:
        start = datetime.datetime.now()
        follow_list_check(browser)

def follow_list_check(browser):
    print('{}'.format('Avaliando usuarios para parar de seguir'))
    users = dbusers.check_unfollow_list()
    if len(users) > 0:
        print('{}'.format('Parando de seguir usuarios'))
        bot.unfollow_people(browser, users)