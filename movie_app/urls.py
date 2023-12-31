from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/<int:id_director>', views.show_one_director, name='director-detail'),
    path('directors/', views.show_directors),
    path('actors/<slug:slug_actor>', views.show_one_actor, name='actor-detail'),
    path('actors/', views.show_all_actor),
]
