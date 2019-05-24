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

    price = forms.IntegerField(required=True, validators=[MinValueValidator(10,
                                message='Minimum price is 10')], widget=forms.TextInput(
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

    screen_size = forms.FloatField(required=True, validators=[MinValueValidator(2, message='Screen size should between 2 and 10'),
                                                              MaxValueValidator(10, message='Screen size should between 2 and 10')],
                                   widget=forms.NumberInput(
                                       attrs={
                                           'class': 'form-control',
                                           'type': 'number'
                                       }
                                   ))

    class Meta:
        model = Phone
        fields = ('id', 'brand', 'phone_model', 'description', 'price', 'image_url', 'screen_size')


class PhoneSearchForm(forms.Form):

    search_phone_model = forms.CharField(required=False, label='Search by model!',
                                    widget=forms.TextInput(attrs={'placeholder': 'search here!'}))

    search_price_min = forms.IntegerField(required=False, label='Min price')

    search_price_max = forms.IntegerField(required=False, label='Max price')

    search_screen_size_min = forms.FloatField(required=False, label='Min screen size')

    search_screen_size_max = forms.FloatField(required=False, label='Max screen size')