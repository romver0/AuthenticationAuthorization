from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'myapp/home.html')


def signupuser(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'myapp/signupuser.html', context)
    else:
        print('request.POST = ', request.POST)
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()  # сохранения пользователя в бд
                login(request, user)  # вход в свой профиль
                # context = {
                #
                # }
                return redirect('currenttodos')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'err': 'Имя пользователя уже используется'
                }
                return render(request, 'myapp/signupuser.html', context)
        else:
            # Tell the user the passwords didn't match
            context = {
                'form': UserCreationForm(),
                'err': 'Пароли не совпадают'
            }
            return render(request, 'myapp/signupuser.html', context)


def logoutuser(request):
    if request.method == 'POST':
        print('сработал logoutuser ', request)
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm(),
        }
        return render(request, 'myapp/login.html', context)
    else:
        # print(User.objects)
        # print('request.POST = ', request.POST)
        # print('',request.POST.get('username'))
        # print('',request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('user = ', user)
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'err': 'Неправильный пароль или имя'
            }
            return render(request, 'myapp/login.html', context)
        else:
            login(request, user)  # вход в свой профиль
            return redirect('currenttodos')


def currenttodos(request):
    return render(request, 'myapp/profile.html')


def gameviews(request):
    return render(request, 'myapp/game.html')


'https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.login'
