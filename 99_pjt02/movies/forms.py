from django import forms
from .models import Movie, Rating


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'poster',)


class RatingForm(forms.ModelForm):
    score = forms.FloatField(
            initial=5,
            max_value=5, min_value=0,
            widget=forms.NumberInput(attrs={'step': '0.1'}),
        )

    class Meta:
        model = Rating
        fields = ('score', 'content',)
