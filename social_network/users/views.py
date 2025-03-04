from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import User, FriendShip, FriendRequest
from django.http import JsonResponse
from django.db.models import Q

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


def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Получаем пользователя по ID
    is_owner = request.user == user
    is_friend = False
    friend_request_sent = FriendRequest.objects.filter(from_user=request.user, to_user=user).exists()
    friend_request = FriendRequest.objects.filter(from_user=request.user, to_user=user)
    if request.user.is_authenticated:
        is_friend = FriendShip.objects.filter(user=request.user, friend=user).exists()
    if request.method == 'POST' and is_owner:
        form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
    else:
        form = UserProfileForm(instance=user)

    context = {'user': user, 'form': form, 'is_owner': is_owner, 'is_friend': is_friend, 'friend_request_sent': friend_request_sent, 'friend_request': friend_request}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('posts:index'))


def friends(request):
    search_query = request.GET.get('search', '')
    show_all = request.GET.get('show_all', None)
    if show_all:
        all_friends = FriendShip.objects.filter(user=request.user)
    elif search_query:
        search_terms = search_query.split()
        q_objects = Q()
        for term in search_terms:
            q_objects |= Q(friend__first_name__icontains=term) | Q(friend__last_name__icontains=term)
        all_friends = FriendShip.objects.filter(q_objects, user=request.user)
    else:
        all_friends = FriendShip.objects.filter(user=request.user)
    received_requests = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)
    return render(request, 'users/friends.html', {'friends': all_friends, 'received_requests': received_requests, 'search_query': search_query})


def add_friend(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)
    if request.user != friend:
        new_friend = FriendShip(user=request.user, friend=friend)
        new_friend.save()
    return HttpResponseRedirect(reverse('users:profile', args=[friend.id]))


def delete_friend(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)
    friendship = FriendShip.objects.filter(user=request.user, friend=friend).first()
    if friendship:
        friendship.delete()
    return HttpResponseRedirect(reverse('users:profile', args=[friend.id]))


def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    if request.user != to_user:
        if not FriendRequest.objects.filter(from_user=request.user, to_user=to_user).exists():
            FriendRequest.objects.create(from_user=request.user, to_user=to_user)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    if not friend_request.is_accepted:
        FriendShip.objects.create(user=request.user, friend=friend_request.from_user)
        FriendShip.objects.create(user=friend_request.from_user, friend=request.user)
        friend_request.is_accepted = True
        friend_request.save()
    return HttpResponseRedirect(reverse('users:friends'))


def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    friend_request.delete()  # Удаляем запрос
    return HttpResponseRedirect(reverse('users:friends'))


def friend_requests(request):
    received_requests = FriendRequest.objects.filter(to_user=request.user, is_accepted=False)
    return render(request, 'users/friends.html', {'received_requests': received_requests})