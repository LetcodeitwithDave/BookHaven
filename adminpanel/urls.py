from django.urls import path
from . import views

urlpatterns = [
    path('admin_header/', views.admin_header, name = 'admin header'),
    path('admin_page/', views.admin_page, name = 'admin page'),
    path('deleteorder/<int:id>', views.deleteorder, name = 'deleteorder'),
    path('admin_order/', views.admin_order, name = 'admin order'),
    path('admin_product/', views.admin_product, name = 'admin products'),
    path('deleteproduct/<int:id>', views.deleteproduct, name = 'deleteproduct'),
    path('admin_user/', views.admin_users, name = 'admin user'),
    path('admin_contact/', views.admin_contact, name = 'admin contact'),
    path('deletecontact/<int:id>', views.contact_delete, name = 'deletecontact'),

]
