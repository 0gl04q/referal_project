# Referal project

## Описание
Referal project - это простой проект реализующий реферальную систему с минимальным интерфейсом

## Основные функции
 - Авторизация осуществляется по номеру телефона. После чего иметируется отправка кода, который сразу отображается на странице подтверждения (специально для демонстрации)
 - В профиле можно ввести реферальный код пользователя. 
 - С помощью API `/profile/api` можно посмотреть всех кто использовал реферальный код пользователя
 - Так же добавлена schema.yml API

## Использование
1. Установите зависимости, выполнив команду `pip install -r requirements.txt`.
2. Перенастройте `settings.py` под себя.

## Зависимости
- Python
- Django
- Django REST Framework
- Библиотеки из файла `requirements.txt`
