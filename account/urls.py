from django.urls import include, re_path as url
from . import views
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url('', include('django.contrib.auth.urls')),
]
