from django.db import models
from music_app1.models import Musician
#from .models import Album
# Create your models here.
class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name