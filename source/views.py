import requests
import os

from django.shortcuts import render
from django.http import HttpResponse


from source import controllers

# Create your views here.
def index(request):
    return HttpResponse(str(controllers.get_rt_rating()) + str(controllers.get_bluray_rating()) + str(controllers.get_tech_spec()))

