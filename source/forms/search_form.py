import django_countries

from django import forms
from django_countries.fields import LazyTypedChoiceField


class SearchForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Movie Title'}), max_length=150)
    country = LazyTypedChoiceField(choices=django_countries.countries)
