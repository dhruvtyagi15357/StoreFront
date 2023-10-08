from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.sayhello),
    path('hello2', views.sayhello2)
]
