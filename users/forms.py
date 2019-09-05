from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #UserRegisterForm is inheriting features form UserCreationForm
    email = forms.EmailField()

    class Meta: #class meta gives us a nested name space for config, and keeps config in one place
        model = User #form.save will save to this User model
        fields = ['username','email','password1','password2'] #passwd1 is input pwd and passwd2 is confirmation pwd

class UserUpdateForm(forms.ModelForm): #form for user attribute model
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']