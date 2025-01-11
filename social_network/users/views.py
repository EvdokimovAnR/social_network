from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем,Вы успешно зарегистрированы!")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm
    context = {'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/profile.html', context)

