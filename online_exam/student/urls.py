from django.urls import path
from student import views
from home import views as hviews
from django.contrib.auth.views import LoginView

urlpatterns=[
path('studentclick', views.studentclick_view),
path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentsignup', views.student_signup_view, name='studentsignup'),
path('student-dashboard', views.student_dashboard_view,name='student-dashboard'),
path('afterlogin', hviews.afterlogin_view,name='afterlogin'),
path('student-exam', views.student_exam_view,name='student-exam'),
path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),

] 