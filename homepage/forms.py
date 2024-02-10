from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django import forms
from django.contrib.auth import password_validation

class RegisterForm(UserCreationForm):    

    username = forms.CharField( widget= forms.TextInput(attrs={'type': 'text', 'name': 'username', 'placeholder': 'Enter Your Fullname', 'required class':'box'}))
    email=forms.EmailField (max_length=100, help_text='Enter a valid email address' ,
                            widget = forms.EmailInput(attrs={'type': 'email','name':'email', 'placeholder': 'Enter Your Email','required class':'box'}))

    password1=forms.CharField(widget = forms.PasswordInput(attrs={'type': 'password','name':'password1', 'placeholder': 'Enter Your Password', 'required class':'box'}),
                              help_text=password_validation.password_validators_help_text_html())
    
    password2=forms.CharField(widget = forms.PasswordInput(attrs={'type': 'password','name':'password2', 'placeholder': 'Confirm Your Password', 'required class':'box'}),
                              help_text=('Just Enter the same password, for confirmation'))
    account_type = forms.ChoiceField(label='Account Type', choices=[('Author', 'Author'), ('User', 'User')], widget=forms.Select(attrs={'class':'box'}))
    

    class Meta:
        model  = User
        fields = ['username', 'email','password1','password2','account_type']
        