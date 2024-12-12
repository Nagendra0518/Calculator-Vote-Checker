from django.urls import path

from voteapp import views

urlpatterns = [
    path('',views.home),
    path('readage',views.votecheck_home),
]