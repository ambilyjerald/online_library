from django.contrib.auth.forms import UserCreationForm
from django import forms

from myapp.models import Login_view, Faculty, Student, Add_Book, Feedback, Transaction


class library_login(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class library_faculty(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('__all__')
        exclude = ('user','admin_approval_status')

class faculty_update_form(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('__all__')
        exclude = ('user', 'admin_approval_status')





class library_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ('user','admin_approval_status')


class student_update_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ('user','admin_approval_status')

class add_book_form(forms.ModelForm):
    class Meta:
        model = Add_Book
        fields = ('__all__')
        exclude = ('staff',)



class dateinput(forms.DateInput):
    input_type = 'date'


class feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('__all__')
        exclude = ('student','reply')

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class IssueBookForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Add_Book.objects.filter(copies=0))
    student = forms.ModelChoiceField(queryset=Student.objects.all())

class RenewBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['due_date']
class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = []
