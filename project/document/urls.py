from django.contrib import admin
from django.urls import path

from . import views

app_name = 'documents'

urlpatterns = [
    path('documents/create/', views.create, name='create'),
    path('documents/', views.read, name='read'),
    path('documents/<int:pk>/read/', views.read_detail, name='detail'),
    path('documents/<int:pk>/edit/', views.update, name='update'),
    path('documents/<int:pk>/delete/', views.delete, name='delete'),
]