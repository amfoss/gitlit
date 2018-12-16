from django.shortcuts import render
from .models import *
import json
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.signals import user_logged_in
from django.apps import apps
usersocialauth = apps.get_model('social_django', 'usersocialauth')




"""
def create_profile(sender, user, request, **kwargs):
    if Profile.objects.filter(user=user):
        pass
    else:
        pr = Profile.objects.create(username=user.username, token=None)
        pr.save()
        token = "03e5d817f468829fd9b3307f55de055461460c1a"
        pr.token=token
        pr.save()
    
user_logged_in.connect(create_profile)

"""


from django.views.generic import DetailView

from django.contrib.auth import logout as auth_logout


def logout(request):
    auth_logout(request)
    return redirect('home')


class UserProfile(DetailView):
    model = User
    template_name = 'user/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        try:
            context['profile'] = Profile.objects.get(user=self.get_object())
        except User.DoesNotExist:
            context['error'] = 'No data found for this user!'
        return context


def about(request):
    return render(request, 'about.html')