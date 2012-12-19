from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'stories.views.index', name='index'),
    url(r'^story/$', 'stories.views.story', name='story'),
    url(r'^vote/$', 'stories.views.vote', name='vote'),
)

