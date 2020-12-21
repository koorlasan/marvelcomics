from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .form import ComicData
from .models import Comic
from .form import ComicInfo
import time
import hashlib
import requests
import json


def dbfill():
    pass


# def save_comic(request, comic):
#    Comic.objects.get(name=title).save()	#    Comic.objects.get(name=title).save()
#    return redirect('index')	#    return redirect('index')
# def fill(request):
#    if 'application/x-www-form-urlencoded' in request.META['CONTENT_TYPE']:
#        print('hi')
#        data = json.loads(request.body)
#        title = data.get('title', None)
#        ....................  # not sure how to save to database
#    pass
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

    else:

        # Дальше надо найти комиксы по названию "title"

        res = requests.get(mygateway).json()
        comics = res['data']['results']
        data = []
        for i, com in enumerate(comics):
            data.append({
                'id': i,
                'title': com['title'],
                'description': com['description'],
                'thumbnail': com['thumbnail']['path'] + '/portrait_xlarge.' + com['thumbnail']['extension'],
                'variants': com['variants'],
                'ean': com['ean'],
                'dates': com['dates'],
            })
            with open('comic-information.json', 'w') as file:
                json.dump(data, file, indent=2)
    return render(request, 'show-results.html', {'comics': data, 'title': title})


def comic_info(request, id):
    new_comic = json.load(open('comic-information.json'))
    for one_comic in new_comic:
        if one_comic['id']:
            return render(request, 'comic-info.html', {'id': id, 'infocomic': new_comic})

