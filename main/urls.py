from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('home_page', views.home_page),
    path('index', views.index),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name="movie_detail"),
    path('serial', views.serial_view),
]