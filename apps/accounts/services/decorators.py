from django.shortcuts import redirect, reverse
from django.conf import settings


def redirect_authenticated_user(func):
    """ Декоратор для отправки на главную страницу если пользователь уже авторизован"""

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('main'))

        return func(request, *args, **kwargs)

    return wrapper
