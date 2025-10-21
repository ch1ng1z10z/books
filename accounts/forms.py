from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'middle_name', 'last_name',
            'birth_date', 'phone', 'address', 'position_applied',
            'education', 'experience_years', 'skills', 'resume'
        ]
