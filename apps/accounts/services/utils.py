import time
from uuid import uuid4
from random import randint

from apps.accounts.models import CustomUser


def unique_invitation_code():
    """ Функция генерации уникального инвайт кода из букв и символов """

    # Создаем уникальный код используя UUID, берем первые 6 символов
    unique_code = str(uuid4())[:6]
    while CustomUser.objects.filter(invitation_code=unique_code):
        unique_code = str(uuid4())[:6]

    return unique_code


def send_verification_code(phone):
    """ Функция генерации и отправки кода на телефон """

    verification_code = randint(1000, 9999)
    # Отправляем письмо на номер <phone> с кодом

    # Ставим задержку
    time.sleep(2)

    return verification_code
