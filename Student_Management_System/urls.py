
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


    path('Hod/Add_Course',views.Add_Course,name='add_course'),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
