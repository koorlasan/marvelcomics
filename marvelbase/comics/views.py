from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Comic
from .apikey import mygateway
import requests
from .models import Comic
from .form import ComicInfo


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        return HttpResponseRedirect(f'show-results/{title}')

    return render(
       request,
       'index.html',
   )

# def save_comic(request, comic):
#    Comic.objects.get(name=title).save()
#    return redirect('index')

def show_results(request, title):
    if request.method == 'POST':
        pass
        # Здесь мы возможно будем сохранять комикс в БД
    else:

        # Дальше надо найти комиксы по названию "title"

        # res = requests.get(mygateway).json()
        # comics = res['data']['results']
        # data = []
        # for com in comics:
        #     data.append({
        #         'title': com['title'],
        #         'description': com['description'],
        #         'thumbnail': com['thumbnail']['path'],
        #     })

        # Для примера
        data = [{
            'title': 'Название',
            'description': 'бла-бла',
            # 'thumbnail': '',
        },
            {
                'title': 'Название2',
                'description': 'Описание2',
                # 'thumbnail': '',
            },
        ]
        return render(request, 'show-results.html', {'comics': data, 'title': title})

