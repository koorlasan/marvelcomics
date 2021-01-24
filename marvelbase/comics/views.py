from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views import generic
from .form import ComicDataForm
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
        if all_comics[id]['id'] >= 0 & all_comics[id]['id'] < len(all_comics):  # здесь что-то не то...
            with open('one-comic-info.json', 'w') as file2:
                json.dump(all_comics[id], file2, indent=2)
            if request.method == "POST":
                save_comic = json.load(open('one-comic-info.json'))
                dbcomic = ComicData(title=save_comic['title'], description=save_comic['description'], thumbnail=save_comic['thumbnail'], dates = (save_comic['dates'][0]['date'])[slice(0, 9)])
                dbcomic.dates = save_comic['dates'][0]['date']
                dbcomic.dates = dbcomic.dates[:10]
                dbcomic.save()
        return render(request, 'comic-info.html', {'id': id, 'infocomic': all_comics[id]})


def my_comics(request):
    my_comic = ComicData.objects.all()
    return render(request, "my-comics.html", {"my_comic": my_comic})


def edit(request, id):
    edit_comic = ComicData.objects.get(id=id)
    if request.method == "POST":
        edit_comic.title = request.POST.get("title")
        edit_comic.description = request.POST.get("description")
        edit_comic.thumbnail = request.POST.get("thumbnail")
        edit_comic.dates = request.POST.get("dates")
        edit_comic.save()
        return HttpResponseRedirect("/")
    return render(request, "edit-comic.html", {'id': id, "edit_comic": edit_comic})


def delete(request, id):
    del_comic = ComicData.objects.get(id=id)
    del_comic.delete()
    return HttpResponseRedirect("/comics/my-comics/")

