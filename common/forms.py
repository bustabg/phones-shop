from django import forms

from .models import AddImage


class AddImageForm(forms.ModelForm):
    image = forms.ImageField(label='Select a file', )

    class Meta:
        model = AddImage
        fields = ('image', )