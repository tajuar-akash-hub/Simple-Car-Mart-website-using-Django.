from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django import forms 

class Registration_form(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']

class change_user_data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']

# handling comment here 


