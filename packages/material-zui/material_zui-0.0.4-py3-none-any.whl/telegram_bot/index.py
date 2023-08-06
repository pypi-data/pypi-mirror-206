import telebot


def setToken(token: str):
    '''https://pypi.org/project/pyTelegramBotAPI'''
    return telebot.TeleBot(token)
