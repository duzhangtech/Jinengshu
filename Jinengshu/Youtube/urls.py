from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^$', "Youtube.views.index"),

)