from . import views
from django.urls import include,path
urlpatterns = [
    path('', views.get_repo, name='get_repo'),
    path('<str:owner>/<str:reponame>', views.get_repodetails, name='get_repodetails'),

]