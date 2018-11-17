from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^republic$', views.republic, name='republic'),

]
