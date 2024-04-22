from django import forms

from apps.accounts.models import CustomUser
from apps.accounts.services.validators import phone_regex


class PhoneNumberForm(forms.Form):
    phone = forms.CharField(max_length=12, validators=[phone_regex], label='Номер телефона')


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=4, label='Код')
    session_phone = None

    def clean_verification_code(self):
        verification_code = self.cleaned_data['verification_code']

        if not CustomUser.objects.filter(phone=self.session_phone, verification_code=verification_code).exists():
            raise forms.ValidationError('Неверный код')

        return verification_code


class InvitationCodeForm(forms.Form):
    invitation_code = forms.CharField(max_length=6, label='Использовать код друга')
    invite_user = None

    def clean_invitation_code(self):
        invitation_code = self.cleaned_data['invitation_code']

        user = CustomUser.objects.filter(invitation_code=invitation_code).first()

        if not user:
            raise forms.ValidationError('Нет такого кода')

        if user == self.invite_user:
            raise forms.ValidationError('Вы не можете ввести свой код')

        return invitation_code
