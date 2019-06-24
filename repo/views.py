from django.shortcuts import render, redirect
from algorithms.repository_rating import RepositoryMetrics
from .forms import DetailForm
# Create your views here.
def get_repodetails(request, owner, reponame):
    headers = {"Authorization": "bearer " + '00374b8690a5e169fe6d1c07eb1d80c90e8e3851'}
    repodetails = RepositoryMetrics(reponame, owner, '00374b8690a5e169fe6d1c07eb1d80c90e8e3851')

    return render(request, 'repo/list_repo.html', {'repodetails': repodetails})

def get_repo(request):
    form = DetailForm(request.POST)
    owner = request.POST.get('owner')
    reponame = request.POST.get('repo')
    if request.method == 'POST':

        return redirect('get_repodetails', owner, reponame)

    else:
        form=DetailForm()
    return render(request, 'repo/name.html', {'form': form})