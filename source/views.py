import requests
import os

from django.shortcuts import render
from django.http import HttpResponse


from source import controllers

# Create your views here.
def index(request):
    return HttpResponse(controllers.get_bluray_rating())

