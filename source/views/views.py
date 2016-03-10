
from django.shortcuts import render
from source.forms.search_form import SearchForm
from source.controllers.cater_controller import CaterController


def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            title = request.GET.__getitem__('movie_title').__str__()

            cater_controller = CaterController(title)
            data = cater_controller.get_data()

            return render(request, 'index.html', {'form': form, 'data': data})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})
