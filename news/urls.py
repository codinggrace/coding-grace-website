from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    # /news/
    url(r'^$', views.index, name='news_index'),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)-(?P<year>\d{4})-(?P<month>\d+)-(?P<day>\d+)/$', views.news, name="news_article"),


    url(r'^all_articles/(?P<chapter>[a-zA-Z_ ]+)/$', views.all_articles_chapter, name="all_news_chapter"),
    url(r'^all_articles/$', views.all_articles, name="all_articles"),
)