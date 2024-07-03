from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import  Album
from .forms import AlbumForm 
from django.views.generic import CreateView,UpdateView,DeleteView

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_app.html', {'form': form})

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.instance.album_app1=request.user
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'album_app.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('musician_list')

class AddAlbumCreateView(CreateView):
    model=Album
    form_class=AlbumForm
    template_name='album_app.html'
    success_url=reverse_lazy('album_create')
    def form_valid(self, form):
         form.instance.album_app1=self.request.user
         return super().form_valid(form)
    
class UpdateAlbumView(UpdateView):
    model=Album
    form_class=AlbumForm
    template_name='album_app.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('album_detail')
        
class DeleteAlbumView(DeleteView):
    model=Album
    form_class=AlbumForm
    template_name='album_app.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('album_delete')

