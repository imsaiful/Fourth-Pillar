from typing import List

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Republic, Ndtv, Indiatoday,Hindustan
import psycopg2
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist

headlines = ""

new_stop_words = ['says', 'khan', 'singh', "'s", "''",
                  'to', 'in', 'for', 'on', 'of', '``', 'and', 'the',
                  'a', 'after', '10', "n't", 'man', 'us', 'first', 'day', "'", '’','‘','new','vs'

                  ]


def getHeadLine(headline):
    global headlines
    for title in headline:
        headlines += title.headline


def index(request):
    global headlines
    headlines = ""
    republic_headline= Republic.objects.order_by('-date')[0:100]
    ndtv_headline = Ndtv.objects.order_by('-date')[0:100]
    hindstan_headline = Hindustan.objects.order_by('-date')[0:100]
    getHeadLine(republic_headline)
    getHeadLine(ndtv_headline)
    getHeadLine(hindstan_headline)
    fd = FreqDist()
    headlines_token = nltk.word_tokenize(headlines)
    stop_words = stopwords.words('english')
    for word in headlines_token:
        if word.lower() not in stop_words and word.lower() not in string.punctuation:
            if word.lower() not in new_stop_words and not word.isnumeric():
                fd[word.lower()] += 1

    keyword = []
    keyword_frequency: List[int] = []
    for word, frequency in fd.most_common(12):
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
    republic_headline = Republic.objects.order_by('-date')[0:5]
    indiatoday_headline = Indiatoday.objects.order_by('-date')[0:5]
    hindustan_headline = Hindustan.objects.order_by('-date')[0:5]
    ndtv_headline = Ndtv.objects.order_by('-date')[0:5]
    message = "Pakistan can't even control its four provinces. It doesn't want Kashmir"
    context = {
        'republic_headline': republic_headline,
        'ndtv_headline': ndtv_headline,
        'indiatoday_headline': indiatoday_headline,
        'hindustan_headline': hindustan_headline,
    }

    return render(request, 'feed/news.html', context)


def republic(request):
    republic_headline = Republic.objects.order_by('-date')[0:100]
    context = {
        'republic_headline': republic_headline,
    }

    return render(request, 'feed/republic.html', context)
