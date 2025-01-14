from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import User


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
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Получаем пользователя по ID
    is_owner = request.user == user
    if request.method == 'POST' and is_owner:
        form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
    else:
        form = UserProfileForm(instance=user)

    context = {'user': user, 'form': form, 'is_owner': is_owner}
    return render(request, 'users/profile.html', context)


# def user_profile(request):

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('posts:index'))
