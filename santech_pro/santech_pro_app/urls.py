from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auf/', views.auf, name='auf')
]