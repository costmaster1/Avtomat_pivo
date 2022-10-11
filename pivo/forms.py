from django import forms
from .models import *


class mony(forms.Form):
    nomin_mony = forms.IntegerField(max_value=10)
