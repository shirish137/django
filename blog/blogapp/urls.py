from django.urls import path
from blogapp import views

urlpatterns = [
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    #http://127.0.0.1:8000/home/10/20
    #path('home/<x>/<y>',views.homepage),
    path('hello',views.helloview),
    path('',views.homepage),
    path('userdashboard',views.user_dashboard),
    path('createblog',views.create_blog),
    path('see_det/<rid>',views.view_details),
    path('publish/<status>/<rid>',views.is_published),
    path('setcookie',views.setcookies),
    path('getcookie',views.getcookies),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('dform',views.djangoForm),
    path('dmform',views.djangomodelform),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
]
