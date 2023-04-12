from argparse import Namespace
import imp
from django.urls import path,include
from .views import *

urlpatterns = [
    path('list',MovieListAV.as_view(),name='movie-list'),
    path('<id>',MovieDetailAV.as_view(),name='movie-details'),
]
