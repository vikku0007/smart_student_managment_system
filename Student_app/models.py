from distutils.command.upload import upload
from doctest import master
import profile
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )

    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to ='media/profile_pic')
   
class Course(models.Model):
    name = models.CharField (max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start = models.CharField(max_length=1000)
    session_end = models.CharField(max_length=1000)


class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    permanent_address =  models.TextField()
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    student_id= models.CharField(max_length=110)
    gender = models.CharField(max_length=10)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add =True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name 

class Staff (models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.TextField(100)
    gender = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add =True)
    update_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.username
class Subjects(models.Model):
    name = models.CharField (max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



