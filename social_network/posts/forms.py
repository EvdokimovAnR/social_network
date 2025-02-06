from django import forms
from .models import Post, Comment


class PostAdd(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст поста'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = Post
        fields = ('content', 'image')


class CommentAdd(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Напишите комментарий...'}))

    class Meta:
        model = Comment
        fields = ('text', )
