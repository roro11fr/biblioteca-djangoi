from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from .models import Book,Inchiriere
    

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']


class BookForm(forms.ModelForm):
     class Meta:
        model=Book
        fields=['name', 'author']

        
def __str__(self):
        return self.name

class SearchF(forms.Form):
    q = forms.CharField(label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))

class SearchU(forms.Form):
    u = forms.CharField(label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    


