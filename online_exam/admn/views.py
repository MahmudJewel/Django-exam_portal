#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse


from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from student import models as SMODEL
from student import forms as SFORM






# Create your views here.
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    context={
    'total_student':SMODEL.Student.objects.all().count(),
    #'total_teacher':TMODEL.Teacher.objects.all().filter(status=True).count(),
    #'total_course':models.Course.objects.all().count(),
    #'total_question':models.Question.objects.all().count(),
    }
    return render(request,'admn/admin_dashboard.html', context)


#=============================start Admin-student ===============================

@login_required(login_url='adminlogin')
def admin_student_view(request):   #side student
    context={
    'total_student':SMODEL.Student.objects.all().count(),
    }
    return render(request,'admn/admin_student.html',context)

@login_required(login_url='adminlogin')
def admin_view_student_view(request): #middle view
    context={
    'students':SMODEL.Student.objects.all(),
    }
    return render(request,'admn/admin_view_student.html',context)


@login_required(login_url='adminlogin')
def update_student_view(request,pk):
    student=SMODEL.Student.objects.get(id=pk)
    user=SMODEL.User.objects.get(id=student.user_id) ### ???
    print('students: ', student, 'user = ', user)
    userForm=SFORM.StudentUserForm(instance=user)
    studentForm=SFORM.StudentForm(request.FILES,instance=student)

    context={
    'userForm':userForm,
    'studentForm':studentForm
    }

    if request.method=='POST':
        userForm=SFORM.StudentUserForm(request.POST,instance=user)
        studentForm=SFORM.StudentForm(request.POST,request.FILES,instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('admin-view-student')
    return render(request,'admn/update_student.html',context)



@login_required(login_url='adminlogin')
def delete_student_view(request,pk):
    student=SMODEL.Student.objects.get(id=pk)
    user=User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/admin-view-student')

#=============================End Admin-student ===============================

