from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
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
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return HttpResponseRedirect('chats:message', recipient_id=recipient_id)
    else:
        form = SendMessageForm()
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('created_at')
    context = {'form': form, 'messages': messages, 'recipient': recipient}
    return render(request, 'chats/chats.html', context)