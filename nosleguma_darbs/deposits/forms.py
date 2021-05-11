from django import forms
from .models import Deposit


class DepositForm(forms.Form):
    deposit = forms.FloatField(label='Deposit:')
    term = forms.FloatField(label='Term:')
    rate = forms.FloatField(label='Rate:')