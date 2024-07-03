from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('list/',views.musician_list,name='musician_list'),
     path('details/<int:id>/',views.EditMusicView.as_view(),name='musician_detail'),
      path('creates/',views.AddMusicCreateView.as_view(),name='musician_create'),
       path('deletes/<int:id>/',views.DeleteMusicView.as_view(),name='musician_delete'),
       
]
