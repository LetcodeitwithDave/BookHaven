from django.urls import path
from . import views

urlpatterns = [
    path('admin_header/', views.admin_header, name = 'admin header'),
    path('admin_page/', views.admin_page, name = 'admin page'),
]