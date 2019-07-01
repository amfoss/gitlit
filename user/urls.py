
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.get_username, name='get_username'),
    path('user/<str:your_name>/', views.list_all, name='list_all'),

]