from django.urls import path
from . import views

urlpatterns = [
    path('', views.cat_home, name='cat_home'),
    path('list/', views.cat_list, name='cat_list'),
    path('cat/<int:pk>/', views.cat_detail, name='cat_detail'),
    path('cat/<int:pk>/<int:action>', views.cat_interact, name='cat_interact'),
]