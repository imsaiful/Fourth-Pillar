from typing import List

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Republic, Ndtv, Indiatoday
import psycopg2
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist

headlines = ""

new_stop_words=['says','khan','singh']
def getHeadLine(headline):
    global headlines
    for title in headline:
        headlines += title.Headline


def index(request):
    republic_headline = Republic.objects.all()
    ndtv_headline = Ndtv.objects.all()
    indiatoday_headline = Indiatoday.objects.all()
    getHeadLine(republic_headline)
    getHeadLine(ndtv_headline)
    getHeadLine(indiatoday_headline)
    fd = FreqDist()
    headlines_token = nltk.word_tokenize(headlines)
    stop_words = stopwords.words('english')
    for word in headlines_token:
        if word not in stop_words and word not in string.punctuation and word not in new_stop_words:
            fd[word.lower()] += 1

    keyword = []
    keyword_frequency: List[int] = []
    for word, frequency in fd.most_common(10):
        keyword.append(word)
        keyword_frequency.append(frequency)

    print(keyword)
    print(keyword_frequency)

    context = {
        "keyword": keyword,
        "keyword_frequency": keyword_frequency,
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


def republic(request):
    republic_headline = Republic.objects.all()
    context = {
        'republic_headline': republic_headline,
    }

    return render(request, 'feed/republic.html', context)
