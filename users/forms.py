
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import Profile
from django.core import validators


class CreateProfile(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='confirm password')
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), validators=[validators.EmailValidator()])
    
    class Meta:
        model = Profile
        fields = ['fullname', 'username','email','phone', 'password1', 'password2', 'address', 'profile_pix']
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'profile_pix':forms.FileInput(attrs={'class':'form-control'}),
            
        }



class UpdateProfile(forms.ModelForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Profile
        fields = ['fullname', 'username','email','phone', 'address', 'profile_pix']
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'profile_pix':forms.FileInput(attrs={'class':'form-control'}),
            
        }


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']