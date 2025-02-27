from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,reverse
from users.models import User
from .models import Message
from .form import SendMessageForm
from django.db.models import Q
from users.models import FriendShip


def chats(request):
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
    context = {'users': users}
    return render(request, 'chats/chats.html', context)


# def message(request, recipient_id):
#     recipient = get_object_or_404(User, id=recipient_id)
#     current_user = request.user
#     friends = FriendShip.objects.filter(user=current_user).values_list('friend', flat=True)
#     users = User.objects.filter(id__in=friends)
#     user_with_message_all = Message.objects.filter(Q(sender=current_user) | Q(recipient=current_user)).values_list('sender', 'recipient').distinct()
#     users_with_message = set()
#     for sender_id, recipient_id in user_with_message_all:
#         if sender_id == current_user.id:
#             users_with_message.add(recipient_id)
#         elif recipient_id == current_user.id:
#             users_with_message.add(sender_id)
#     users_with_dialogue = User.objects.filter(id__in=users_with_message)
#     users_with_last_message = []
#     for user in users_with_dialogue:
#         last_message = Message.objects.filter(
#             (Q(sender=current_user) & Q(recipient=user)) |
#             (Q(sender=user) & Q(recipient=current_user))
#         ).order_by('-created_at').first()
#         users_with_last_message.append({
#             'user': user,
#             'last_message': last_message,
#             'last_message_time': last_message.created_at if last_message else None
#         })
#     if request.method == 'POST':
#         form = SendMessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.recipient = recipient
#             message.save()
#             print(recipient_id)
#             return HttpResponseRedirect(reverse('chats:message', args=[recipient_id]))
#
#     else:
#         form = SendMessageForm()
#
#     messages = Message.objects.filter(
#         (Q(sender=request.user) & Q(recipient=recipient)) |
#         (Q(sender=recipient) & Q(recipient=request.user))
#     ).order_by('created_at')
#
#     try:
#         last_message = Message.objects.filter(
#             (Q(sender=request.user) & Q(recipient=recipient)) |
#             (Q(sender=recipient) & Q(recipient=request.user))
#         ).latest('created_at')
#     except Message.DoesNotExist:
#         last_message = None
#     context = \
#         {
#         'form': form,
#         'messages': messages,
#         'recipient': recipient,
#         'users': users_with_dialogue,
#         'last_message': last_message,
#         'users_with_last_message': users_with_last_message
#     }
#     return render(request, 'chats/message.html', context)

def message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    current_user = request.user

    # Получаем список друзей текущего пользователя
    friends = FriendShip.objects.filter(user=current_user).values_list('friend', flat=True)
    users = User.objects.filter(id__in=friends)

    # Поиск среди пользователей
    search_query = request.GET.get('search', '')
    if search_query:
        search_terms = search_query.split()
        q_objects = Q()
        for term in search_terms:
            q_objects |= Q(first_name__icontains=term) | Q(last_name__icontains=term)
        users = users.filter(q_objects)  # Фильтруем пользователей по поисковому запросу

    # Формируем список пользователей с последним сообщением
    users_with_last_message = []
    for user in users:
        last_message = Message.objects.filter(
            (Q(sender=current_user) & Q(recipient=user)) |
            (Q(sender=user) & Q(recipient=current_user))
        ).order_by('-created_at').first()
        users_with_last_message.append({
            'user': user,
            'last_message': last_message,
            'last_message_time': last_message.created_at if last_message else None
        })

    # Обработка формы отправки сообщения
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return HttpResponseRedirect(reverse('chats:message', args=[recipient_id]))
    else:
        form = SendMessageForm()

    # Все сообщения между двумя конкретными пользователями
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('created_at')

    # Находим последнее сообщение между двумя конкретными пользователями
    try:
        last_message = Message.objects.filter(
            (Q(sender=request.user) & Q(recipient=recipient)) |
            (Q(sender=recipient) & Q(recipient=request.user))
        ).latest('created_at')
    except Message.DoesNotExist:
        last_message = None

    # Формируем контекст для шаблона
    context = {
        'form': form,
        'messages': messages,
        'recipient': recipient,
        'users': users,
        'last_message': last_message,
        'users_with_last_message': users_with_last_message,
        'search_query': search_query  # Передаем поисковый запрос в шаблон
    }
    return render(request, 'chats/message.html', context)