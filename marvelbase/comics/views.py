from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from .form import ComicDataForm, ComicInfoForm
from .models import ComicData
import time
import hashlib
import requests
import json


def dbfill():
    pass


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        return HttpResponseRedirect(f'show-results/{title}')

    return render(
        request,
        'index.html',
    )


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
        all_comics = json.load(open('comic-information.json'))
        for one_comic in all_comics:
            if one_comic['id'] >= 0 & one_comic['id'] < len(all_comics):  # здесь что-то не то...
                with open('one-comic-info.json', 'w') as file2:
                    json.dump(all_comics[id], file2, indent=2)
                if request.method == "POST":
                    save_comic = json.load(open('one-comic-info.json'))
                    dbcomic = ComicData(request.POST)
                    #(title=save_comic['title'],description=save_comic['description'], thumbnail=save_comic['thumbnail'], variants=save_comic['variants'], ean=save_comic['ean'], dates=save_comic['dates'])
                    dbcomic.title = save_comic['title']
                    dbcomic.description = save_comic['description']
                    dbcomic.thumbnail = save_comic['thumbnail']
                    dbcomic.variants = save_comic['variants']
                    dbcomic.ean = save_comic['ean']
                    dbcomic.dates = save_comic['dates']
                    dbcomic.save()

            return render(request, 'comic-info.html', {'id': id, 'infocomic': all_comics[id]})
