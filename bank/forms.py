from django import forms

from .models import Transfer


class TransferFunds(forms.ModelForm):
    name = forms.CharField()
    funds = forms.IntegerField()
    class Meta:
        model = Transfer
        fields=('name','funds')


