from django.conf.urls import url
from .views import *
from django.views.generic import TemplateView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('<slug:reponame>', RepoProfile.as_view(), name='repository-profile'),
]