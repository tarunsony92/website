from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('laptop/',views.laptoppage,name='laptop'),
    path('login/',views.signin,name='login'),
    path('emailid/',views.emailid,name='emailid'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('register/',views.register,name='register'),
    path('user/', views.user, name='user'),
    path('orders/', views.orders, name='orders'),
    path('logout/', views.signout, name='logout'),
    path('buynow/', views.buynow, name='buynow'),
    path('checkout/', views.checkout, name='checkout'),
    path('changepass/', views.changepass, name='changepass'),
    path('mycart/', views.mycart, name='mycart'),
    path('update_cart/', views.update_cart, name='update_cart'),

]