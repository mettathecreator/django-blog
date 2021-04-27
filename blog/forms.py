from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# Create your forms here.

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

class SignIn(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    # email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

class CommentCreateForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('email', 'body')