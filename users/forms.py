from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        '''
        Meta.fields just displays the default settings of username and password,
        to which we then add an age field
        '''
        # fields = UserCreationForm.Meta.fields + ('age',)

        '''
        This approach specifies exactly which fields to use
        '''
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age')
