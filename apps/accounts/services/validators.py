from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^((\+7)|8)\d{10}$', message="Формат номера: '+79999999999' or '89999999999'.")
