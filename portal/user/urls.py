from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^about/$', about, name="about"),
    url(r'^@(?P<username>[\w.@+-]+)/$', UserProfile.as_view(), name="user"),

]

