from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'edit', ProfileEditView.as_view(),name='app_profiles_edit' ),
    url(r'', 'app.profiles.views.default',name='app_profiles_default' ),
)
