from django.urls import path
from teacher import views
from django.contrib.auth.views import LoginView
from home import views as hviews 
from admn import views as AVIEW

urlpatterns = [
path('teacherclick', views.teacherclick_view),
path('teachersignup', views.teacher_signup_view,name='teachersignup'),
path('teacherlogin', LoginView.as_view(template_name='teacher/teacherlogin.html'),name='teacherlogin'),
path('teacher-dashboard', views.teacher_dashboard_view,name='teacher-dashboard'),
path('afterlogin', hviews.afterlogin_view,name='afterlogin'),

path('teacher-exam', views.teacher_exam_view,name='teacher-exam'),
path('teacher-add-exam', views.teacher_add_exam_view,name='teacher-add-exam'),
path('teacher-view-exam', views.teacher_view_exam_view,name='teacher-view-exam'),
path('delete-exam/<int:pk>', views.delete_exam_view,name='delete-exam'),

path('teacher-question', views.teacher_question_view,name='teacher-question'),
path('teacher-add-question', views.teacher_add_question_view,name='teacher-add-question'),
path('teacher-view-question', views.teacher_view_question_view,name='teacher-view-question'),
path('see-question/<int:pk>', views.see_question_view,name='see-question'),
path('remove-question/<int:pk>', views.remove_question_view,name='remove-question'),

path('teacher-view-student', views.teacher_view_student,name='teacher-view-student'),
]