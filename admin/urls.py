from django.urls import path

from . import views

urlpatterns = [
    path('auth', views.auth, name='auth'),

    path('poll/create', views.create_poll, name='create_poll'),
    path('poll/delete', views.delete_poll, name='delete_poll'),
    path('poll/change', views.change_poll, name='change_poll'),

    path('question/delete', views.delete_question, name='delete_question'),
    path('question/create', views.create_question, name='create_question'),
    path('question/change', views.change_question, name='change_question')
]