from django.contrib import admin
from django.urls import path
from admn import views
from django.contrib.auth.views import LogoutView,LoginView


urlpatterns = [
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='admn/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),


    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view,name='delete-student'),

]