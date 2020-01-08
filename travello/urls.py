from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/dash/', views.user, name='user'),
    path('register/', views.register, name='register'),
    path('upload', views.upload, name='upload'),
]
