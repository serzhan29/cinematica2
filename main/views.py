from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.db.models import Q


from .models import Movie, Category



def home_page(request):
    return render(request, "main/cinematica.html")


class MoviesView(ListView):
    def get(self, request):
        categories = Category.objects.all()
        movies = Movie.objects.filter(Q(category__id=1))
        cartoons = Movie.objects.filter(Q(category__id=2))
        serial = Movie.objects.filter(Q(category__id=3))
        all = Movie.objects.all()
        return render(request, 'main/cinematica.html', {"movie_list": movies,
                                                        "cartoon_list": cartoons,
                                                        "serial_list": serial,
                                                        "categories": categories,
                                                        "all": all})


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "main/movie_detail.html", {"movie": movie})


class OneFilm(DetailView):
    def one_film(self, request):
        model = Movie
        template_name = "main/movie_detail.html"
        one_film = Movie.objects.filter(id=1)
        return render(request, template_name, {"one_film": one_film})


def index(request):
    return render(request, "main/index.html")



def serial_view(request):
    categories = Category.objects.all()
    serial = Movie.objects.filter(Q(category__id=3))
    all = Movie.objects.all()
    return render(request, 'main/serial.html',
                      {"serial_list": serial,
                       "categories": categories,
                       "all": all})

