from django import forms
from django.core.validators import EmailValidator

from .models import Question
from . import enums


class CreateQuestionForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
                            attrs={
                                'class': 'form-control'
                            }
                            ))

    email = forms.CharField(required=True, widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }
                                ))

    question = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    # answer = forms.CharField(widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))

    # is_approved = forms.BooleanField(widget=forms.CheckboxInput())


    class Meta:
        model = Question
        fields = ('name', 'email', 'question')


class EditQuestionForm(forms.ModelForm):
    # status = forms.CharField(disabled=True, widget=forms.TextInput(
    #                         attrs={
    #                             'class': 'form-control'
    #                         }
    #                         ))
    name = forms.CharField(disabled=True, widget=forms.TextInput(
                            attrs={
                                'class': 'form-control'
                            }
                            ))
    email = forms.CharField(disabled=True, widget=forms.TextInput(
                            attrs={
                                'class': 'form-control'
                            }
                            ))
    question = forms.CharField(disabled=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    answer = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Question
        fields = ('status', 'name', 'email', 'question', 'answer')