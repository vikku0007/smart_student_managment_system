
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/",views.BASE, name='base'),
    path("",views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name ='doLogin'),
    path('doLogout',views.doLogout,name ='logout'),
    path('Profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),
    path('Hod/Home',HOD_views.HOME,name='Hod_home'),
    path('Hod/Add_student',views.Add_student,name='Add_student'),
    path('Hod/View_student',views.View_student,name='View_student'),
    path('Hod/Edit_student/<str:id>',views.Edit_student,name='Edit_student'),
    path('Hod/Update_student',views.Update_student,name='Update_student'),
    path('Hod/delete_student/<str:admin>',views.Delete_student,name='delete_student'),
    
    # All Staff page linke
    path('Hod/Add_Staff',views.Add_Staff,name='add_staff'),
    path('Hod/View_Staff',views.View_Staff,name='view_staff'),
    path('Hod/Edit_Staff/<str:id>',views.Edit_Staff,name='edit_staff'),
    path('Hod/Update_Staff',views.Update_Staff,name='update_staff'),
    path('Hod/Delete_Staff/<str:id>',views.Delete_Staff,name='delete_staff'),
#  All Course page linke
    path('Hod/Add_Course',views.Add_Course,name='add_course'),
    path('Hod/View_Course',views.View_Course,name='view_course'),
    path('Hod/Edit_Course/<str:id>',views.Edit_Course,name='edit_course'),
    path('Hod/Update_Course',views.Update_Course,name='update_course'),
    path('Hod/Delete_Course/<str:id>',views.Delete_Course,name='delete_course'),



#  All Subjects page linke
    path ('Hod/Add_Subjects',views.Add_Subjects,name='add_subjects'),
    path('Hod/View_Subjects',views.View_Subjects,name='view_subjects'),
    path('Hod/Edit_Subjects/<str:id>',views.Edit_Subjects,name='edit_subjects'),
    path('Hod/Update_Subjects',views.Update_Subjects,name='update_subjects'),
    path('Hod/Delete_Subjects/<str:id>',views.Delete_Subjects,name='delete_subjects'),

#  All Session page linke
    path ('Hod/Add_Session',views.Add_Session,name='add_session'),
    path ('Hod/View_Session',views.View_Session,name='view_session'),
    path ('Hod/Edit_Session/<str:id>',views.Edit_Session,name='edit_session'),
    path ('Hod/Update_Session',views.Update_Session,name='update_session'),
    path('Hod/Delete_Session/<str:id>',views.Delete_Session,name='delete_session'),

    

   
   



] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
