from .models import *
from django.shortcuts import render, redirect
from django.views.generic import DetailView


class RepoProfile(DetailView):
    model = Repository
    template_name = 'repo/profile.html'
    slug_field = 'reponame'
    slug_url_kwarg = 'reponame'

