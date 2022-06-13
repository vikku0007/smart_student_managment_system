from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Student_app.models import Course,CustomUser, Session_Year,Student,Staff,Subjects
@login_required(login_url='/')
def HOME(request):
    
    students_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subjects_count = Subjects.objects.all().count()
    context = {
        'students_count'  : students_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subjects_count' : subjects_count,
    }
    # print(students_count,staff_count,course_count,subjects_count)
    return render(request,'Hod/Home.html',context)
   