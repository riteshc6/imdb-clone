from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from imdb.models import Movie, Review
from imdb.forms import MovieUploadForm, EditUploadForm

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
    if request.method == 'POST':
        form = MovieUploadForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.posted_by = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieUploadForm()
    return render(request, 'imdb/add_movie.html', {'form': form})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'imdb/movie_detail.html', {'movie': movie})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = EditUploadForm(instance=movie)
    if request.method == 'POST':
        form = EditUploadForm(request.POST, instance=movie)
        if form.is_valid():
            print("valid ----------------------------------- ")
            movie = form.save(commit=False)
            movie.posted_by = request.user
            movie.save()
            return redirect('movie_detail', pk=pk)
    return render(request, 'imdb/edit_movie.html', {'form': form})
