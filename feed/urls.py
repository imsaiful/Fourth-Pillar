from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^republic$', views.republic, name='republic'),
    url(r'^ndtv$', views.ndtv, name='ndtv'),
    url(r'^indiatoday$', views.indiatoday, name='indiatoday'),
    url(r'^hindustan$', views.hindustan, name='hindustan'),
    url(r'^logout$', views.logout_view, name='logout'),

]
