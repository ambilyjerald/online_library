from datetime import timedelta, datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class Login_view(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Faculty(models.Model):
    user = models.ForeignKey(Login_view,on_delete=models.CASCADE, related_name='faculty')
    admin_approval_status = models.BooleanField(default = 0)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.CharField(max_length=20)
    id_number = models.IntegerField()
    image = models.ImageField(upload_to='documents/')
    # is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Student(models.Model):
    user = models.ForeignKey(Login_view,on_delete=models.CASCADE,related_name='student')
    admin_approval_status = models.BooleanField(default = 0)
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
    # is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Add_Book(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name='add_book')
    category = models.CharField(max_length=200)
    book_name = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    book_number = models.IntegerField()
    isbn = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    copies = models.IntegerField()
    cost = models.IntegerField()
    image = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.book_name

class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "feedback_student")
    date = models.DateTimeField(default=timezone.now)
    # date = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 250)
    feedback = models.TextField()
    reply = models.TextField(blank = True, null = True)


class Transaction(models.Model):
    book = models.ForeignKey(Add_Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField()
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.book.book_name} issued by {self.student.user.username}'

class Fine(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Fine for {self.transaction.book.book_name}'




