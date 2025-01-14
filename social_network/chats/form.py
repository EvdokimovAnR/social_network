from django import forms
from .models import Message


class SendMessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'write-message', 'placeholder': 'Введите сообщение'}))

    class Meta:
        model = Message
        fields = ('content',)
