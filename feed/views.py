from typing import List
from django.contrib.auth import get_user_model,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm, LoginForm
from .models import Republic, Ndtv, Indiatoday,Hindustan,Thehindu,Zeenews
import psycopg2
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist

headlines = ""

new_stop_words = ['says', 'khan', 'singh', "'s", "''",
                  'to', 'in', 'for', 'on', 'of', '``', 'and', 'the',
                  'a', 'after', '10', "n't", 'man', 'us', 'first', 'day', "'", '’','‘','new','vs','india','top'

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
    thehindu_headline = Thehindu.objects.order_by('-date')[0:100]
    zeenews_headline = Zeenews.objects.order_by('-date')[0:100]

    getHeadLine(republic_headline)
    getHeadLine(ndtv_headline)
    getHeadLine(hindstan_headline)
    getHeadLine(thehindu_headline)
    getHeadLine(zeenews_headline)
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
    hindu_headline = Ndtv.objects.order_by('-date')[0:5]
    zeenews_headline = Ndtv.objects.order_by('-date')[0:5]
    context = {
        'republic_headline': republic_headline,
        'ndtv_headline': ndtv_headline,
        'indiatoday_headline': indiatoday_headline,
        'hindustan_headline': hindustan_headline,
        'hindu_headline':hindu_headline,
        'zeenews_headline':zeenews_headline
    }

    return render(request, 'feed/news.html', context)


def republic(request):
    republic_headline = Republic.objects.all().order_by('-id')
    paginator = Paginator(republic_headline, 10)
    page = request.GET.get('page')
    try:
        republic_headline = paginator.page(page)
    except PageNotAnInteger:
        republic_headline = paginator.page(1)
    except EmptyPage:
        republic_headline = paginator.page(paginator.num_pages)

    context = {
        'republic_headline': republic_headline,
    }

    return render(request, 'feed/republic.html', context)

def ndtv(request):
    ndtv_headline = Ndtv.objects.order_by('-id')[0:20]
    context = {
        'ndtv_headline': ndtv_headline,
    }

    return render(request, 'feed/ndtv.html', context)

def indiatoday(request):
    indiatoday_headline = Indiatoday.objects.order_by('-date')[0:20]
    context = {
        'indiatoday_headline': indiatoday_headline,
    }

    return render(request, 'feed/indiatoday.html', context)

def hindustan(request):
    hindustan_headline = Hindustan.objects.order_by('-date')[0:20]
    context = {
        'hindustan_headline': hindustan_headline,
    }

    return render(request, 'feed/hindustan.html', context)



class LoginForm(generic.CreateView):
    print("login")
    form_class = LoginForm
    template_name = "feed/SignUp.html"

    def get(self, request):
        title = "Login to Vote"
        form = self.form_class(None)
        context = {
            "title": title,
            "form": form,

        }
        return render(request, self.template_name, context)

    def Post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                print("try")
                username = request.POST['username']
                username = User.objects.get(email=username).username  # Get username with email
                password = request.POST['password']
                validate_email(username)  # If it's a valid email
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('')

            except:
                print("except")
                UserModel = get_user_model()

                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('')
        else:
            print(form.errors)

def logout_view(request):
    logout(request)
    return index(request)