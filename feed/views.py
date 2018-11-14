from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'feed/index.html', {})


def news(request):
    print("hello world")
    message = "Pakistan can't even control its four provinces. It doesn't want Kashmir"
    return render(request, 'feed/news.html', {"message": message})
