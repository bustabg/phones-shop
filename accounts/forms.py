from django import forms

from .models import ProfileUser


class UserCreationForm(forms.ModelForm):
    profile_picture = forms.CharField(required=True, widget=forms.URLInput(
                                attrs={
                                    'class': 'form-control'
                                }
                                ))

    phone_number = forms.CharField(required=True, widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }
                                ))

    class Meta:
        model = ProfileUser
        fields = ('id', 'profile_picture', 'phone_number')
