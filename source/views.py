from django.shortcuts import render
from .forms import SearchForm
from source import view_models


def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            title = request.GET.__getitem__('movie_title').__str__()
            rt_rating = view_models.get_rt_rating(title)
            bluray_rating = view_models.get_bluray_rating(title)
            tech_specs = view_models.get_tech_spec(title)
            price = view_models.get_price(title)

            return render(request, 'index.html', {'form': form, 'rt_rating': rt_rating, 'bluray_rating': bluray_rating, 'tech_specs': tech_specs, 'price': price})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
