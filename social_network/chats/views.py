from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,reverse
from users.models import User
from .models import Message
from .form import SendMessageForm
from django.db.models import Q


def chats(request):
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
    context = {'users': users}
    return render(request, 'chats/chats.html', context)


def message(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
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
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('created_at')

    try:
        last_message = Message.objects.filter(
            (Q(sender=request.user) & Q(recipient=recipient)) |
            (Q(sender=recipient) & Q(recipient=request.user))
        ).latest('created_at')
    except Message.DoesNotExist:
        last_message = None
    context = \
        {
        'form': form,
        'messages': messages,
        'recipient': recipient,
        'users': users,
        'last_message': last_message,
        'users_with_last_message': users_with_last_message
    }
    return render(request, 'chats/message.html', context)
