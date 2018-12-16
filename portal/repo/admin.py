from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save

admin.site.register(Repository)
admin.site.register(Topic)