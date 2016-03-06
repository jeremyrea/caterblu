from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import SearchForm
from source import view_models


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            return render(request, 'index.html', {'form': form, 'rt_rating': view_models.get_rt_rating(request.GET.__getitem__('movie_title').__str__()), 'bluray_rating': view_models.get_bluray_rating(request.GET.__getitem__('movie_title').__str__()), 'tech_specs': view_models.get_tech_spec(request.GET.__getitem__('movie_title').__str__())})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
