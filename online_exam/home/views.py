from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
#from teacher import models as TMODEL
from student import models as SMODEL
#from teacher import forms as TFORM
from student import forms as SFORM
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request, 'home/home.html')

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def afterlogin_view(request):
    #return redirect('student-dashboard')
    #'''
    if is_student(request.user):
        print('A student', request.user)
        return HttpResponseRedirect('student-dashboard') 
    else:
        print('an admin', request.user)
        return redirect('admin-dashboard')  
    #'''
    '''elif is_teacher(request.user):
        accountapproval=TMODEL.Teacher.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('teacher/teacher-dashboard')
        else:
            return render(request,'teacher/teacher_wait_for_approval.html')'''

