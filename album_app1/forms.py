from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['musician', 'name', 'release_date', 'rating']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)])
        }