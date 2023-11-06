from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


# Create your views here.

def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_first=True), 'rating')
    movies = Movie.objects.annotate(
        new_field_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(234),
        new_budget=F('budget') + 100,
        ry=F('year') * F('rating')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))

    data = {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    }
    return render(request, 'movie_app/all_movies.html', context=data)


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=data)


def show_directors(request):
    directors = Director.objects.all()
    data = {
        'directors': directors
    }
    return render(request, 'movie_app/all_directors.html', context=data)


def show_one_director(request, id_director: int):
    director = Director.objects.get(id=id_director)
    data = {
        'director': director
    }
    return render(request, 'movie_app/one_director.html', context=data)


def show_all_actor(request):
    actors = Actor.objects.all()
    data = {
        'actors': actors
    }
    return render(request, 'movie_app/all_actors.html', context=data)


def show_one_actor(request, slug_actor: str):
    actor = Actor.objects.get(slug=slug_actor)
    data = {
        'actor': actor
    }
    return render(request, 'movie_app/one_actor.html', context=data)
