from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        report = dict()
        new_user = User.objects.create_user(login, email, pass1)
        if new_user is None:
            report['mess'] = 'Реєстарція невдала!'
        else:
            report['mess'] = 'Ви успішно зареєстровані!'

        url = f'http://127.0.0.1:8000/user/confirm?email={email}'
        subject = 'Підтвердження реєстрації'
        body = f"""
            <hr />
            <h3>Для підтвердження реєстрації перейдіть за посиланням</h3>
            <h4>
                <a href="{url}">{url}</a>
            </h4>
            <hr />
        """
        # відправка підтвердження
        success = send_mail(subject, '', 'eCourses', [email], fail_silently=False, html_message=body)
        if not success:
            report['info'] = 'Ваша пошта недійсна!'
        else:
            report['info'] = f"""
                Дякуємо, що обрали  нас!♥♥♥
            """
    return render(request, 'user/reg_res.html', context=report)


def confirm(request):
    
    email = request.GET.get('email')

    user = User.objects.filter(email=email)
    
    group = User.groups.filter(name='ConfirmedUsers')
    User.groups.add(group)

    return render(request, 'user/confirm.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        report = dict()
        check_user = authenticate(request, username=_login, password=_pass1)

        if check_user is None:
            report['mess'] = 'Нажаль користувач не знайдений ☹'
        else:
            report['mess'] = 'Ви авторизовані!☺'
            login(request, check_user)
        return render(request, 'user/log_res.html', context=report)


