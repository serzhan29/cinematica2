from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('index', views.Index.as_view(), name="index"),
    path('search/', views.Search.as_view(), name="search"),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('__debug__/', include('debug_toolbar.urls')),
]

