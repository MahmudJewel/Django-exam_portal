from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.contrib.auth.models import Group
from .forms import StudentUserForm, StudentForm
from home import models as HMODEL
#from teacher import models as TMODEL
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')


def student_signup_view(request):
    userForm=StudentUserForm()
    studentForm=StudentForm()
    if request.method=='POST':
        userForm=StudentUserForm(request.POST)
        studentForm=StudentForm(request.POST, request.FILES)
        #print(userForm,studentForm)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False) #This doesn't save the form data immediately.
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    context={
        'userForm':userForm,
        'studentForm':studentForm,
    }
    return render(request,'student/studentsignup.html',context)


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    context={
    
    #'total_course':HMODEL.Course.objects.all().count(),
    #'total_question':HMODEL.Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context) 
