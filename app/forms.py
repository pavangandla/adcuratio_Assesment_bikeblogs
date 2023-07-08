from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

        help_texts={'username': ''}


class BikeForm(forms.ModelForm):
    class Meta:
        model=Bike
        fields='__all__'
