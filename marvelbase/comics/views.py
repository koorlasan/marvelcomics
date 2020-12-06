from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .form import ComicData
from .models import Comic
from .form import ComicInfo
import time
import hashlib
import requests



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
    publickey = "058789c458e2a5c666c1878c07fdc37b"
    privatekey = "277608909782d353e372ac535074386bdb3d8815"
    ts = round(time.time())
    mystring = str(ts) + privatekey + publickey
    hash_object = hashlib.md5(mystring.encode())
    mygateway = f'https://gateway.marvel.com/v1/public/comics?orderBy=title&titleStartsWith={title}&format=comic&formatType=comic&ts={str(ts)}&apikey={publickey}&hash={hash_object.hexdigest()}'
    if request.method == 'POST':
        pass
        # Здесь мы возможно будем сохранять комикс в БД
    else:

        # Дальше надо найти комиксы по названию "title"

         res = requests.get(mygateway).json()
         comics = res['data']['results']
         data = [{
            'title': '',
            'description': '',
            'thumbnail': '',
        },
            {
                'title': '',
                'description': '',
                'thumbnail': '',
            },
        ]
         for com in comics:
             data.append({
                 'title': com['title'],
                 'description': com['description'],
                 'thumbnail': com['thumbnail']['path']+'/portrait_xlarge.'+com['thumbnail']['extension'],
             })

    return render(request, 'show-results.html', {'comics': data, 'title': title})


def comic_info(request, title):
    comic = ComicData.objects.get()
    return render(request, 'comic-info.html', {'title': title})

#class ComicDetailView(generic.DetailView):
#    model = Comic

