from django.shortcuts import render
from django.views.generic import ListView, View
from django.db.models import Q


from .models import Movie, Rating


class MoviesView(ListView):
    def get(self, request):
        movies = Movie.objects.filter(Q(category__id=1))
        cartoons = Movie.objects.filter(Q(category__id=2))
        serial = Movie.objects.filter(Q(category__id=3))
        all = Movie.objects.all().order_by('-id')
        popular = Rating.objects.order_by('star')
        popular_serial = Rating.objects.filter(movie__category__id=3).order_by('star')
        return render(request, 'main/cinematica.html', {"movie_list": movies,
                                                        "cartoon_list": cartoons,
                                                        "serial_list": serial,
                                                        "all": all,
                                                        "popular": popular,
                                                        "popular_serial": popular_serial,
                                                        }
                      )


class MovieDetailView(View):
    def get(self, request, slug):
        popular = Rating.objects.order_by('star')
        movie = Movie.objects.get(url=slug)
        return render(request, "main/movie_detail.html", {"movie": movie,
                                                          "popular": popular,
                                                          })


class Search(ListView):
    model = Movie  # Добавляем атрибут model
    template_name = 'main/index.html'
    context_object_name = 'movie_list'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Movie.objects.filter(title__icontains=query)
        else:
            return Movie.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class Index(ListView):
    def get(self, request):
        all = Movie.objects.all()
        return render(request, 'main/index.html', {
                                                        "all": all,
                                                        }
                      )