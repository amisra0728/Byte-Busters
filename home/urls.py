from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('', hello_world),
    path('register', RegisterUser.as_view()),
    path('login', CustomAuthToken.as_view()),
    path('users', UserView.as_view()),
    path('flat', FlatCreateAPIView.as_view()),
    path('flatsearch',GetFlatSearchAPI.as_view(),name='flatsearch'),
    path('flatsearch/', get_flats_by_location.as_view(), name='get_flats_by_location'),
    path('flatmate', FlatmateCreateAPIView.as_view()),
    path('flatmatesearch/', get_flatmates_by_location.as_view(), name='get_flatmates_by_location'),
    path('flatmatesearch',GetFlatmateSearchAPI.as_view())
]