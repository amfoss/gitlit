
from algorithms.user_rating import UserMetrics
from django.shortcuts import render, redirect
from django.shortcuts import render

from .forms import NameForm

def list_all(request, your_name):
    usermetrics = UserMetrics(your_name, "<token-here>")
    print(usermetrics.basePoints)
    return render(request, 'user/list_all.html', {"usermetrics": usermetrics})

def get_username(request):
    form = NameForm(request.POST)
    username = request.POST.get('your_name')
    if request.method == 'POST':

        return redirect('list_all', username)

    else:
        form=NameForm()
    return render(request, 'user/name.html', {'form': form})