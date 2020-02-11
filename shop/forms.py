from django import forms
from .models import Goods,Photos,User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,label='E-mail')
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput,help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Password again',widget=forms.PasswordInput,help_text='Enter password agein')
    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1!=password2:
            errors = {'password2':ValidationError('Password dont match...',code='password_mismatch')}
            raise ValidationError(errors)

    def save(self,commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model=User
        fields = ('username','email','password1','password2','first_name','last_name')

class NewGoodsForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ['image','name','info','current_price','old_price','category','sub_category']

class PhotosForm(forms.ModelForm):
    class Meta:
        model=Photos
        fields=['location','small_image','big_image']

