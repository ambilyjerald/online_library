from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from myapp.forms import library_student, feedback_form
from myapp.models import Student, Feedback


def read_student(request):
    data=Student.objects.all()
    return render(request,'student_dash/student_details.html',{'studentkey':data})

def del_student(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('student_detail')

def up_student(request,id):
    n=Student.objects.get(id=id)
    form= library_student(instance=n)
    if request.method=="POST":
        form= library_student(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect("student_detail")
    return render(request,"student_dash/student_update.html",{"form":form})



def student_feedback(request):
    feedback_form_data = feedback_form()
    current_student_object = Student.objects.get(user = request.user)
    if request.method == 'POST':
        feedback_form_data = feedback_form(request.POST)
        if feedback_form_data.is_valid():
            feedback_object = feedback_form_data.save(commit = False)
            feedback_object.student = current_student_object
            feedback_object.save()
            return redirect('studentdash')
    current_student_object = Student.objects.get(user=request.user)
    return render(request, 'student_dash/student_feedback.html',{'feedback_form_data':feedback_form_data,'current_student_object':current_student_object})


def student_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    current_student_object = Student.objects.get(user=request.user)
    return render(request,'student_dash/student_view_feedbacks.html',{'feedback_objects':feedback_objects,'current_student_object':current_student_object})


def student_feedback_delete(request, id):
    feedback_object = Feedback.objects.get(id = id)
    feedback_object.delete()
    current_student_object = Student.objects.get(user=request.user)
    return redirect('student_view_feedbacks',{'current_student_object':current_student_object})
