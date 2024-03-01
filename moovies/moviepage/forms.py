from django import forms
from .models import Moovie

class FilmForm(forms.Form):
    CATEGORY_CHOICES = [
        (None, '----'),
        ('actor', 'Actor'),
        ('producer', 'Producer'),
        ('year', 'Year'),
    ]

    name = forms.CharField(max_length=30, required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)


class FilmDetailForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, label='Film name:')
    producer = forms.CharField(max_length=30, required=True)
    actors = forms.CharField(max_length=200, required=True)
    year = forms.IntegerField(required=True)

class CreateFilmForm(forms.ModelForm):

    class Meta:
        model = Moovie
        fields = ['name', 'release_year', 'producer', 'actors']