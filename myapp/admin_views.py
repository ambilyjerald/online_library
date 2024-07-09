from django.shortcuts import redirect, render

from myapp.forms import add_book_form
from myapp.models import Faculty, Add_Book, Feedback, Student, Transaction


def faculty_approval_requests(request):
    faculty_objects = Faculty.objects.filter(admin_approval_status = 0)
    return render(request,"admin_dash/admin_faculty_approval_requests.html",{'faculty_objects':faculty_objects})

def approve_faculty(request, id):
    faculty_object = Faculty.objects.get(id = id)
    faculty_object.admin_approval_status = 1
    faculty_object.save()
    return redirect('faculty_approval_requests')

def remove_faculty_request(request, id):
    faculty_object = Faculty.objects.get(id=id)
    user_object = faculty_object.user
    user_object.delete()
    return redirect('faculty_approval_requests')

def student_approval_requests(request):
    student_objects = Student.objects.filter(admin_approval_status = 0)
    return render(request,"admin_dash/admin_student_approval_requests.html",{'student_objects':student_objects})

def approve_student(request, id):
    student_object = Student.objects.get(id = id)
    student_object.admin_approval_status = 1
    student_object.save()
    return redirect('student_approval_requests')

def remove_student_request(request, id):
    student_object = Student.objects.get(id=id)
    user_object = student_object.user
    user_object.delete()
    return redirect('student_approval_requests')

def admin_read_faculty(request):
    data=Faculty.objects.all()
    return render(request,'admin_dash/faculty_details.html',{'facultykey':data})

def admin_del_faculty(request,id):
    data=Faculty.objects.get(id=id)
    data.delete()
    return redirect('faculty_detail')

def admin_read_student(request):
    data=Student.objects.all()
    return render(request,'admin_dash/student_details.html',{'studentkey':data})

def admin_del_student(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('student_detail')




def admin_book_table(request):
    table = Add_Book.objects.all()
    return render(request,'admin_dash/book_details.html',{'data':table})

def admin_delete_book(request,id):
    data = Add_Book.objects.get(id=id)
    data.delete()
    return redirect("book_table")

def admin_view_feedbacks(request):
    feedback_objects = Feedback.objects.all()
    return render(request,'admin_dash/admin_view_feedbacks.html',{'feedback_objects':feedback_objects})



def admin_feedback_reply(request, id):
    feedback_object = Feedback.objects.get(id = id)
    if request.method == 'POST':
        reply = request.POST.get('reply')
        feedback_object.reply = reply
        feedback_object.save()
        return redirect('admin_view_feedbacks')
    return render(request,'admin_dash/admin_feedback_reply.html',{'feedback_object':feedback_object})


def admin_feedback_delete(request,id):
    feedback_object = Feedback.objects.get(id=id)
    feedback_object.delete()
    return redirect('admin_view_feedbacks')

def admin_view_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, 'admin_dash/admin_view_transactions.html', {'transactions': transactions})


