from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'photo/edit/(?P<id>\d*)', PhotoProfileView.as_view(),name='app_profiles_photo_edit' ),
    url(r'', 'app.profiles.views.default',name='app_profiles_default' ),
)
