from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from .models import Phone, Brand


class CreateBrandForm(forms.ModelForm):
    brand = forms.CharField(required=True, validators=[RegexValidator(r'^[A-Z][a-z]+$',
                                message='Brand should start with capital letter followed by small letters!')],
                                widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                },

                                ))

    class Meta:
        model = Brand
        fields = ('id', 'brand')


class CreatePhoneForm(forms.ModelForm):

    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(
                            attrs={
                                  'class': 'form-control'
                            }
                            ))

    phone_model = forms.CharField(required=True, widget=forms.TextInput(
                            attrs={
                                'class': 'form-control'
                            }
                            ))

    description = forms.CharField(required=True, widget=forms.Textarea(
                            attrs={
                                'class': 'form-control'
                            }
                            ))

    price = forms.IntegerField(required=True, validators=[MinValueValidator(1)], widget=forms.TextInput(
                            attrs={
                                'class': 'form-control',
                                'type': 'number'
                            }
                            ))

    image_url = forms.CharField(required=True, widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }
                                ))

    screen_size = forms.FloatField(required=True, validators=[MinValueValidator(2), MaxValueValidator(10)],
                                   widget=forms.NumberInput(
                                       attrs={
                                           'class': 'form-control',
                                           'type': 'number'
                                       }
                                   ))

    class Meta:
        model = Phone
        fields = ('id', 'brand', 'phone_model', 'description', 'price', 'image_url', 'screen_size')
