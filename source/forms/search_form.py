from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Movie Title'}), max_length=150)
