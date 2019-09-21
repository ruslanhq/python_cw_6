from django import forms
from django.forms import widgets


class EntryForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=2000, required=True, label='Text', widget=widgets.Textarea)
