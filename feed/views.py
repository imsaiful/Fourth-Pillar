from typing import List
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm, LoginForm
from .models import Republic, Ndtv, Indiatoday, Hindustan, Thehindu, Zeenews
import psycopg2
import nltk
from nltk.corpus import stopwords
import string
from nltk.probability import FreqDist
from django.db.models import Q

headlines = ""

new_stop_words = ['says', 'khan', 'singh', "'s", "''",
                  'to', 'in', 'for', 'on', 'of', '``', 'and', 'the',
                  'a', 'after', '10', "n't", 'man', 'us', 'first', 'day', "'", '’', '‘', 'new', 'vs', 'india', 'top',
                  '...', 'life',
                  'gets', 'back', 'takes'

                  ]


def getHeadLine(headline):
    global headlines
    for title in headline:
        headlines += title.headline


def index(request):
    global headlines
    headlines = ""
    republic_headline = Republic.objects.order_by('-date')[0:100]
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
    for word, frequency in fd.most_common(11):
        keyword.append(word)
        keyword_frequency.append(frequency)

    print(keyword)
    print(keyword_frequency)

    keyword.append("end")
    keyword_frequency.append(0)
    context = {
        "keyword": keyword,
        "keyword_frequency": keyword_frequency,
    }

    return render(request, 'feed/index.html', context)


def news(request):
    republic_headline = Republic.objects.order_by('-id')[0:5]
    indiatoday_headline = Indiatoday.objects.order_by('-id')[0:5]
    hindustan_headline = Hindustan.objects.order_by('-id')[0:5]
    ndtv_headline = Ndtv.objects.order_by('-id')[0:5]
    hindu_headline = Thehindu.objects.order_by('-id')[0:5]
    zeenews_headline = Zeenews.objects.order_by('-id')[0:5]
    context = {
        'republic_headline': republic_headline,
        'ndtv_headline': ndtv_headline,
        'indiatoday_headline': indiatoday_headline,
        'hindustan_headline': hindustan_headline,
        'hindu_headline': hindu_headline,
        'zeenews_headline': zeenews_headline
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


class SignUpForm(generic.CreateView):
    form_class = SignUpForm
    template_name = "feed/SignUp.html"

    def get(self, request):
        title = "SignUp - Save 4th pillar"
        form = self.form_class(None)
        context = {
            "title": title,
            "form": form,
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            print("form valid")
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('feed:index')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return index(request)


def stats(request):
    np = Ndtv.objects.filter(sentiment='positive').count()
    nn = Ndtv.objects.filter(sentiment='negative').count()

    rp = Republic.objects.filter(sentiment='positive').count()
    rn = Republic.objects.filter(sentiment='negative').count()

    htp = Hindustan.objects.filter(sentiment='positive').count()
    htn = Hindustan.objects.filter(sentiment='negative').count()

    thp = Thehindu.objects.filter(sentiment='positive').count()
    thn = Thehindu.objects.filter(sentiment='negative').count()

    znp = Zeenews.objects.filter(sentiment='positive').count()
    znn = Zeenews.objects.filter(sentiment='negative').count()

    itp = Indiatoday.objects.filter(sentiment='positive').count()
    itn = Indiatoday.objects.filter(sentiment='negative').count()

    total_positive = np + rp + htp + thp + znp + itp
    total_negative = nn + rn + htn + thn + znn + itn

    lp = [np, rp, htp, thp, znp, itp]
    ln = [nn, rp, htn, thn, znn, itn]

    percentage = (total_positive / (total_positive + total_negative)) * 100

    context = {
        "lp": lp,
        "ln": ln,
        "positive": total_positive,
        "negative": total_negative,
        "percentage": percentage
    }

    return render(request, "feed/stats.html", context)


class FindKeyWordNews(generic.ListView):
    template_name = "feed/keyword.html"

    def get_queryset(self):
        keyword = self.kwargs.get("keyword")
        if keyword:
            query_list = Republic.objects.filter(Q(headline__icontains=keyword))
        return query_list



