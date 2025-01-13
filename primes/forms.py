from django import forms

class PrimeForm(forms.Form):
    number = forms.IntegerField(min_value=2, label='Enter a number')