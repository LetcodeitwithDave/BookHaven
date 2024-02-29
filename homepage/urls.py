from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('index/', views.index, name = 'index'),
    path('page/', views.page, name = 'page'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutpage, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('about/', views.about, name = 'about'),
    path('cart/', views.cart, name = 'cart'),
    path('deletecart/<int:id>', views.deletecart, name = 'deletecart'),
    path('deleteAll', views.deleteAll, name = 'deleteAll'),
    path('shop/', views.shop, name = 'shop'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('order/', views.order, name = 'order'),
    path('cartdelete/', views.cartdelete, name = 'cartdelete'),
    path('contact/', views.contact, name = 'contact'),
    path('search/', views.search_page, name = 'search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)