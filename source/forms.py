from django import forms


class SearchForm(forms.Form):
    movie_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Movie Title'}), max_length=150, required=False)

