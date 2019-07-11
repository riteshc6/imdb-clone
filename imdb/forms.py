from django import forms
from .models import Movie


class MovieUploadForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'stars', 'director', 'description', 'image_path')


class EditUploadForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'stars', 'director', 'description')
  