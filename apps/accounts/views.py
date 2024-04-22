from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from apps.accounts.models import CustomUser, InvitationCodeUsers
from apps.accounts.forms import PhoneNumberForm, VerificationCodeForm, InvitationCodeForm
from apps.accounts.services.utils import send_verification_code
from apps.accounts.services.decorators import redirect_authenticated_user


def main(request):
    return render(request, 'accounts/main.html')


@redirect_authenticated_user
def login_by_phone_number(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']

            request.session['phone'] = phone

            user, created = CustomUser.objects.get_or_create(phone=phone)

            user.verification_code = send_verification_code(phone)

            user.save()

            return redirect('verify')
    else:
        form = PhoneNumberForm()
    return render(request, 'registration/login.html', {'form': form})


@redirect_authenticated_user
def phone_verify_code(request):
    if request.method == "POST":
        session_phone = request.session['phone']

        form = VerificationCodeForm(request.POST)
        form.session_phone = session_phone

        if form.is_valid():
            code = form.cleaned_data['verification_code']

            user = CustomUser.objects.get(phone=session_phone, verification_code=code)

            user.verification_code = None
            user.save()

            login(request, user)

            return redirect('profile')
    else:
        form = VerificationCodeForm()

    # Пишу нижнюю строку только для получения кода сразу на сайне
    code = CustomUser.objects.get(phone=request.session['phone']).verification_code

    return render(request, 'registration/verify.html', {'form': form, 'code': code})


@login_required
def profile(request):
    if request.method == "POST":
        invite_user = request.user

        form = InvitationCodeForm(request.POST)
        form.invite_user = invite_user

        if form.is_valid():
            invitation_code = form.cleaned_data['invitation_code']

            main_user = get_object_or_404(CustomUser, invitation_code=invitation_code)

            InvitationCodeUsers.objects.create(main_user=main_user, invite_user=invite_user)
    else:
        form = InvitationCodeForm()

    context = {'title': 'Профиль'}

    if request.user.check_invite():
        context['main_user'] = request.user.invite.first().main_user
    else:
        context['form'] = form

    return render(request, 'accounts/profile.html', context)
