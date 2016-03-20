
from django.shortcuts import render
from source.forms.search_form import SearchForm
from source.controllers.cater_controller import CaterController


def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            title = request.GET.__getitem__('title').__str__()

            cater_controller = CaterController(title)
            try:
                data = cater_controller.get_data()
                return render(request, 'index.html', {'status': 200, 'form': form, 'data': data})
            except ValueError:
                return render(request, 'index.html', {'status': 204, 'form': form})

    else:
        form = SearchForm()

    return render(request, 'index.html', {'status': 200, 'form': form})
