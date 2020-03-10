from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_home, name='cat_home'),
    path('list', views.cat_list, name='cat_list'),
]