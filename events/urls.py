from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    # /events/
    url(r'^$', views.index, name='event_index'),

    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/(?P<event_id>\d+)/$', views.event, name="event_detail"),

)