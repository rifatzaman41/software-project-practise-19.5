from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Musician
from .forms import MusicianForm
from django.views.generic import CreateView,UpdateView,DeleteView
def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'music_app.html', {'musicians': musicians})

def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'music_app.html', {'form': form})

def musician_create(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.instance.music_app1=request.user
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm()
    return render(request, 'music_app.html', {'form': form})

def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('musician_list')

class AddMusicCreateView(CreateView):
    model=Musician
    form_class=MusicianForm
    template_name='music_app.html'
    success_url=reverse_lazy('musician_create')
    def form_valid(self,form):
        form.instance.music_app1=self.request.user
        return super().form_valid(form)
    
class  EditMusicView(UpdateView):
     model=Musician
     form_class=MusicianForm
     template_name='music_app.html'
     pk_url_kwarg='pk'
     success_url=reverse_lazy('musician_detail')

class DeleteMusicView(DeleteView):
     model=Musician     
     form_class=MusicianForm
     template_name='music_app.html'
     pk_url_kwarg='pk'
     success_url=reverse_lazy('musician_detail')
    