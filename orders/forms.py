from django import forms
from .models import *

class CheckoutContentFrom(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)

    