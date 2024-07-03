from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:pk>/',views.UpdateAlbumView.as_view(),name='album_detail'),
    path('create/',views.AddAlbumCreateView.as_view(),name='album_create'),
    path('delete/<int:pk>/',views.DeleteAlbumView.as_view(),name='album_delete'),
    
]