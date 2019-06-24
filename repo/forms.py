from django import forms

class DetailForm(forms.Form):
    owner = forms.CharField(label='owner', max_length=100)
    repo = forms.CharField(label='repo', max_length=100)