from django.shortcuts import render
from music_app1.models import Musician
from django.views.generic import CreateView
def home(request):
   data=Musician.objects.all()

   return render(request,'index.html',{'data':data}) 