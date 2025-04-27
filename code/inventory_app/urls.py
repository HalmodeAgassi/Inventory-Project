from django.contrib import admin
from django.urls import path
from .views import Index, RegisterView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', RegisterView.as_view()),
]