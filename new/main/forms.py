# forms.py
from django import forms

class MyForm(forms.Form):
    text_field = forms.CharField()
    medical = forms.FileField()
    varient = forms.FileField()
    expression = forms.FileField()
