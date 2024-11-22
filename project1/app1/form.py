from django import forms
from . models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LogginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email','password')