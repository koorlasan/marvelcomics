from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Comic
from .apikey import mygateway
import requests
from .models import Comic
from .form import ComicInfo


def index(request):
    if request.method == 'POST':
        res = requests.get(mygateway).json()
        comics = res['data']['results']
        for com in Comic:
            comics = {
                'title': comics[0]['title'],
                'description': comics[0]['description'],
                'thumbnail': comics[0]['thumbnail']['path'],
            }
#    title = Comic.objects.all()
#    description = Comic.objects.all()
#    thumbnail = Comic.objects.all()

#    return render(
#        request,
#        'index.html',
#        context={'title': title, 'description': description,
#                 'thumbnail': thumbnail
#                 }
#    )
# def save_comic(request, comic):
#    Comic.objects.get(name=title).save()
#    return redirect('index')
