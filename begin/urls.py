from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:id>', views.detail_view, name = 'detail'),
    path('profile', views.profile, name = 'profile'),
    path('search', views.search, name = 'search'),
]