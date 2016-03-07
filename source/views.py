from multiprocessing.pool import ThreadPool
from django.shortcuts import render
from .forms import SearchForm
from source import view_models


def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            title = request.GET.__getitem__('movie_title').__str__()
            
            pool = ThreadPool(processes=5)
            async_rt_rating = pool.apply_async(view_models.get_rt_rating, (title,))
            async_bluray_rating = pool.apply_async(view_models.get_bluray_rating, (title,))
            async_tech_specs = pool.apply_async(view_models.get_tech_spec, (title,))
            async_price = pool.apply_async(view_models.get_price, (title,))
            async_artwork = pool.apply_async(view_models.get_artwork, (title,))
            
            rt_rating = async_rt_rating.get()
            bluray_rating = async_bluray_rating.get()
            tech_specs = async_tech_specs.get()
            price = async_price.get()
            artwork = async_artwork.get()

            return render(request, 'index.html', {'form': form, 'rt_rating': rt_rating, 'bluray_rating': bluray_rating, 'tech_specs': tech_specs, 'price': price, 'artwork': artwork})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
