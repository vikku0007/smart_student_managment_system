from distutils.command.build_scripts import first_line_re
from http.client import UNSUPPORTED_MEDIA_TYPE
from django.shortcuts import render,redirect
from Student_app.EmailBackEnd import EmailBackEnd 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Student_app.models import Course,CustomUser, Session_Year,Student,Staff,Subjects

def BASE(request):
    return render(request,"base.html")



def LOGIN(request):
    return render(request,"login.html")


 
def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, 
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type =='1':
                return redirect('Hod_home')
            elif user_type =='2':
                return HttpResponse('This is  Staff page')
            elif user_type == '3':
                 return HttpResponse('This is  Student page')
        else:
            messages.error(request,'Email and Password Are Invalide.....')
            return redirect('login')
    else:
        messages.error(request,'Email and Password Are Invalide.....')
    return redirect('login') 
@login_required(login_url='/')
def doLogout(request):

    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    # return HttpResponse("hello")
    return render (request,'profile.html',context)

@login_required(login_url='/')

def PROFILE_UPDATE(request):
    if request.method =="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic,first_name,last_name,email,username,password )
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password !=" ":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != " ":
               customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your  Profile Updated Successfuly....')
            return redirect('profile')            
        except:                 
            messages.error(request,'Failed to  Updated Your Profile Successfuly....')

    return render(request,'profile.html')

@login_required(login_url='/')
def Add_student(request):
    course = Course.objects.all()
    session_year =Session_Year.objects.all()
    if request.method =="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        permanent_address = request.POST.get('permanent_address')
        course = request.POST.get('course')
        session_year_id = request.POST.get('session_year_id')
        


        # print(profile_pic,first_name,last_name,username,student_id,email,password,gender,permanent_address,course,session_year_id,)
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Is Already Taken.....')
            return redirect('Add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username Is Already Taken....')
            return redirect('Add_student')
        else:
            user = CustomUser (
                first_name = first_name,
                last_name = last_name,
                username= username,
                email = email,
                profile_pic  = profile_pic ,
                user_type = 3
               


            )
        user.set_password(password)
        user.save()
        course = Course.objects.get(id = course) 
        session_year_id = Session_Year.objects.get(id = session_year_id)
            
        student = Student(
                        admin = user,
                        permanent_address  = permanent_address ,
                        session_year_id = session_year_id,
                        course = course,
                        gender = gender
        )
        student.save()
        messages.success(request, user.first_name + " " + user.last_name + 'Student Successfully Saved....')
        return redirect('Add_student')
    
    context = {
        'course' : course,
        'session_year' : session_year,
    }

    return render(request, "Hod/Add_student.html", context)
@login_required(login_url='/')
def View_student(request):
    student = Student.objects.all()
    print(student)
    context = {
        "student":student,
    }
    # return HttpResponse("hello")
  
    return render(request,"Hod/View_student.html",context)
@login_required(login_url='/')
def Edit_student(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    # print("student,course,session_year")
    context = {
        'student':student,
        'course':course,
        'session_year':session_year
    }
    return render(request,'Hod/Edit_student.html',context)
@login_required(login_url='/')
def Update_student(request):
    if request.method =="POST":
        student_id = request.POST.get('student_id')
    
        profile_pic = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        permanent_address = request.POST.get('permanent_address')
        course = request.POST.get('course')
        session_year_id = request.POST.get('session_year_id')
        user = CustomUser.objects.get(id = student_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.username =username
        user.emali = email

        if password != None and password !=" ":
                user.set_password(password)
        if profile_pic != None and profile_pic != " ":
               user.profile_pic = profile_pic
        user.save()
        student = Student.objects.get(admin = student_id)
        student.permanent_address = permanent_address
        student.gender = gender

        course = Course.objects.get(id = course)
        student.course = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year 
        student.save()
        messages.success(request,'Record Are Successfully Updated....')
        return redirect('View_student')
        # print (profile_pic,student_id)
    return render(request,'Hod/Edit_student.html')
@login_required(login_url='/')
def Delete_student(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Student Delete Successfully.....')
    return redirect('View_student')  
@login_required(login_url='/')
def Add_Course(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request, "Add_Course successfully.....")
        return redirect('add_course')
        print(course_name)

    return render(request,'Hod/Add_Course.html')
@login_required(login_url='/')
def View_Course(request):
    course = Course.objects.all()
    context = {
        "course" : course,
    }
   
    return render(request,'Hod/View_Course.html',context)
@login_required(login_url='/')
def Edit_Course(request,id):
    course = Course.objects.get(id = id)
    context = {
        
        'course':course,
        
    }
    
    return render(request,'Hod/Edit_Course.html',context)
@login_required(login_url='/')
def Update_Course(request):
    if request.method =="POST":
        name = request.POST.get('name')
        course_id =request.POST.get('course_id')
        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Update Course successfully....')
        return redirect('view_course') 

    return request(render,'Hod/Edit_Course.html')
@login_required(login_url='/')
def Delete_Course(request,id):
    course= Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Delete Course successfully....')
    return redirect('view_course')
@login_required(login_url='/')
def Add_Staff(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('permanent_address')
        gender = request.POST.get('gender')
        
        print(profile_pic,first_name,last_name,username,email,password,address,gender)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is Already Taken !....')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already Taken !....')
            return redirect('add_staff')
        else:
            user = CustomUser(
                            profile_pic = profile_pic,
                            first_name = first_name,
                            last_name = last_name,
                            username  = username,
                            email = email,
                            password = password,
                            user_type= 2
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                gender = gender
            )
            staff.save()
            messages.success(request,'Add Staff successfully.....')
    return render(request,'Hod/Add_Staff.html')
@login_required(login_url='/')
def View_Staff(request):
    staff = Staff.objects.all()

    context = { 
        'staff':staff,
    }
    return render (request,'Hod/View_Staff.html',context)
@login_required(login_url='/')
def Edit_Staff(request,id):
    staff = Staff.objects.get(id = id)
    context ={
        'staff':staff,
    }
    return render(request,'Hod/Edit_Staff.html',context)
@login_required(login_url='/')
def Update_Staff(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        
        
        
        
        
        # course = Course.objects.get(id = course_id)
        user = CustomUser.objects.get(id = staff_id)
        user.first_name = first_name
        user.last_name = last_name 
        user.username = username
        user.email = email
         
        if password != None and password !=" ":
                user.set_password(password)
        if profile_pic != None and profile_pic != " ":
               user.profile_pic = profile_pic
        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.gender = gender
        staff.save()
        messages.success(request,'The Update is successfully.....')
        return redirect('view_staff')
        
    return render(request,'Hod/Edit_Staff.html')
@login_required(login_url='/')
def Delete_Staff(request,id):
    user = CustomUser.objects.get(id = id)
    user.delete()
    messages.success(request,'Staff  is delete successfully....')
    return redirect('view_staff')
@login_required(login_url='/')
def Add_Subjects(request):
    
        course = Course.objects.all()
        staff = Staff.objects.all()
        if request.method =="POST":
            subjects_name = request.POST.get ('subjects_name')
            course_id = request.POST.get ('course_id')
            staff_id = request.POST.get ('staff_id')

            course = Course.objects.get (id = course_id)
            staff = Staff.objects.get (id = staff_id)

            subjects = Subjects (
                name = subjects_name,
                course = course,
                staff = staff, 
            ) 


            subjects.save()
            print(subjects)
            messages.success(request,' Subjects are  Successfully Add....')
            return redirect('add_subjects')

        context = {
            'course':course,
            'staff':staff,
        }
       
        return render (request,'Hod/Add_Subjects.html',context)
  
@login_required(login_url='/')
def View_Subjects(request):
    subjects = Subjects.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request,'Hod/View_Subjects.html',context)
@login_required(login_url='/')
def Edit_Subjects(request,id):
    subjects = Subjects.objects.get(id = id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context =  {
        'subjects' : subjects,
        'course' : course,
        'staff' : staff,
    }

    return render(request,'Hod/Edit_Subjects.html',context)
@login_required(login_url='/')
def Update_Subjects(request):
    if request.method == "POST": 
        subjects_id = request.POST.get('subjects_id')
        subjects_name = request.POST.get('subjects_name')
        course_id = request.POST.get('course_id')
        staff_id= request.POST.get('staff_id')
       
        course = Course.objects.get(id = course_id)

        staff = Staff.objects.get(id = staff_id)
        subjects = Subjects (
            id = subjects_id,
            name = subjects_name,
            course = course,
            staff = staff,
        )
        
        subjects.save()
        messages.success(request,'The Update is successfully.....')
        return redirect('view_subjects')
    return render(request,'Hod/Edit_Subjects.html')

def Delete_Subjects(request,id):
    subjects = Subjects.objects.filter(id = id)
    subjects.delete()
    messages.success(request,' The Subjects are Successfully....Delete....')
    redirect('view_subjects')

def Add_Session(request):
    if request.method =="POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year (
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,'The Session year are successfully add.....')
        return redirect('add_session')
    return render(request,'Hod/Add_Session.html')
def View_Session(request):
    session = Session_Year.objects.all()
    context = {
        'session' :session,
    }
    return render(request,'Hod/View_Session.html',context)

def Edit_Session(request,id):
    session = Session_Year.objects.filter(id = id)

    context = {
        'session' : session,

    }
    return render(request,'Hod/Edit_Session.html',context)
def Update_Session(request):
    if request.method =="POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('sessionn_year_end')

  
        session = Session_Year (
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'update is successfully......')
        return redirect('view_session')
    return render(request,'Hod/Edit_Session.html')
def Delete_Session(request,id):
    session = Session_Year.objects.filter(id = id)
    session.delete()
    messages.success(request,'This Is Deleteing Successfully.....')
    return redirect('view_session')