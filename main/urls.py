from django.urls import path

from . import views

urlpatterns = [
    path('poll', views.get_user_poll, name='get_user_poll'),
    path('polls', views.get_user_polls, name='get_user_polls'),

    path('poll/get', views.get_poll, name='get_poll'),
    path('polls/get', views.get_polls, name='get_polls'),
    path('answer/create', views.create_answers, name='create_answers'),
]
