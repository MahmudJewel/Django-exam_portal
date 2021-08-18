from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from home import views

urlpatterns = [
    path('', views.home),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    path('logout', LogoutView.as_view(template_name='home/logout.html'),name='logout'),
]