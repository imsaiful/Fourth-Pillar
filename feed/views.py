from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Republic,Ndtv,Indiatoday


def index(request):
    republic_headline = Republic.objects.order_by('-Date')[0:5]

    context = {
        'republic_headline': republic_headline,
    }
    return render(request, 'feed/index.html', context)


def news(request):
    republic_headline = Republic.objects.order_by('Date')[0:5]
    indiatoday_headline = Indiatoday.objects.order_by('Date')[0:5]
    ndtv_headline = Ndtv.objects.order_by('Date')[0:5]
    message = "Pakistan can't even control its four provinces. It doesn't want Kashmir"
    context = {
        'republic_headline': republic_headline,
        'ndtv_headline': ndtv_headline,
        'indiatoday_headline': indiatoday_headline,
        'message': message,
    }

    return render(request, 'feed/news.html', context)
