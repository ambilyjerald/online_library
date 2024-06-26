from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Faculty(models.Model):
    user = models.ForeignKey(Login_view,on_delete=models.CASCADE, related_name='faculty')
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    id_number = models.IntegerField()
    image = models.ImageField(upload_to='documents/')

    def __str__(self):
        return self.name




class Student(models.Model):
    user = models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='student')
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    roll_number = models.IntegerField()
    id_number = models.IntegerField()
    image = models.ImageField(upload_to='documents/')

    def __str__(self):
        return self.name

class Add_Book(models.Model):
    seller=models.ForeignKey(staff,on_delete=models.CASCADE,related_name='add_book')
    category = models.CharField(max_length=200)
    book_name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    book_number = models.IntegerField()
    isbn = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    copies = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return self.name
