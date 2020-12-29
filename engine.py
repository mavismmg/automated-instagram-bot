import browser, dbusers
import constantes
import datetime
import time


def init(webdriver, tag, flag):
    constantes.init()
    browser.login(webdriver, tag, flag)


def update(webdriver):
    return