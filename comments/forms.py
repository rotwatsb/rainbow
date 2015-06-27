from django import forms
from comments.models import Comment, Conversation
from django.contrib.auth.models import User
import datetime

class ConversationForm(forms.ModelForm):
    
    name = forms.CharField(max_length=256, help_text="Conversation?")

    time_created = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.datetime.now())

    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Conversation
        fields = ('name',)

    
class CommentForm(forms.ModelForm):

    text = forms.CharField(max_length=1024, help_text="comment text")

    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
