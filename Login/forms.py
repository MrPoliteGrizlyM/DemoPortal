from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       PasswordResetForm)



class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2')

    def save(self,commit=True):
        user = super(RegForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password')


class PasswordReset(PasswordResetForm):

    class Meta:
        fields = ('email')

    def __init__(self, *args, **kwargs):
        super(PasswordReset, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
