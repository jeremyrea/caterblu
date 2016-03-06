import requests
import os

from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm
from source import view_models


# Create your views here.
def index(request):
    # return HttpResponse(controllers.get_bluray_rating())
    # return render(request, 'index.html')
    if request.method == 'GET':
        form = SearchForm(initial=request.GET.dict())


        return render(request, 'index.html', {'form': form, 'rt_rating': view_models.get_rt_rating(request.GET.__getitem__('movie_title').__str__()), 'bluray_rating': view_models.get_bluray_rating(request.GET.__getitem__('movie_title').__str__()), 'tech_specs': view_models.get_tech_spec(request.GET.__getitem__('movie_title').__str__())})
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
