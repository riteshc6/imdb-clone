from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from imdb.models import Movie, Review

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'imdb/movie_list.html', {'movies': movies})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()
    return render(request, 'imdb/signup.html', {'form': form})


def add_movie(request):
    pass    


def movie_detail(request):
    pass