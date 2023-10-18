from django.shortcuts import render, get_object_or_404
from .models import Movie


# Create your views here.

def show_all_movies(request):
    movies = Movie.objects.all()

    for movie in movies:
        movie.save()

    data = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies.html', context=data)


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=data)
