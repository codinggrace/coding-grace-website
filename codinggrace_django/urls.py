from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='codinggrace_django/profile.html'), name="account_profile"),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),

    url(r'^$', 'codinggrace_django.views.home', name='home'),
    url(r'^chapters/$', 'codinggrace_django.views.chapters', name='chapters'),
    url(r'^chapters/(?P<chapter>[a-zA-Z0-9_-]+)/$', 'codinggrace_django.views.chapter', name='chapter'),
    url(r'^chapters/ireland/dublin/posts/(?P<year>\d{4})-(?P<month>\d+)-(?P<day>\d+)-(?P<slug>[a-zA-Z0-9_-]+)/$', 'codinggrace_django.views.news_redirect', name="news_redirect"),
    url(r'^codeofconduct/$', 'codinggrace_django.views.codeofconduct', name="codeofconduct"),
    url(r'^colophon/$', 'codinggrace_django.views.colophon', name="colophon"),
    url(r'^resources/$', 'codinggrace_django.views.resources', name="resources"),
    url(r'^sponsors/$', 'codinggrace_django.views.sponsors', name="sponsors"),

    # url(r'^blog/', include('blog.urls')),
    url(r"^events/", include("events.urls", namespace="events")),
    url(r"^news/", include("news.urls", namespace="news")),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

)
