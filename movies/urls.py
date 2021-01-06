from django.urls import path

from . import views


urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<int:pk>/", views.MovieDetalView.as_view())
]
