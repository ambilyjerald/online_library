from django.contrib.auth.forms import UserCreationForm
from django import forms

from myapp.models import Login_view, Faculty, Student, Add_Book, Feedback


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
        exclude = ('user','status1')


class library_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('__all__')
        exclude = ('user','status2')
class add_book_form(forms.ModelForm):
    class Meta:
        model = Add_Book
        fields=('__all__')
        exclude=('staff',)

class student_feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject','feedback')


class dateinput(forms.DateInput):
    input_type = 'date'


