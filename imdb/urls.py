from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie_detail/', views.movie_detail, name='movie_detail'),
]
