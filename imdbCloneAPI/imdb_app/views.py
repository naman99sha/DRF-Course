# from django.shortcuts import render
# from .models import *
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     return JsonResponse({'movies':list(movies.values())})

# def movie_details(request, id):
#     movie = Movie.objects.get(id=id)
#     return JsonResponse({"movie":movie.name})