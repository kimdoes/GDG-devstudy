from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(''.views.index),
    path('/get', views.get_api),
    path("/post",views.post_api),
]
