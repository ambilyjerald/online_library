from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

# from myapp.filters import book_filter_form
from myapp.forms import library_student, feedback_form, BookSearchForm, IssueBookForm, RenewBookForm, ReturnBookForm
from myapp.models import Student, Feedback, Add_Book, Transaction, Fine


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
    return render(request,'student_dash/student_view_feedbacks.html',{'feedback_objects': feedback_objects,'current_student_object': current_student_object})


def student_feedback_delete(request, id):
    feedback_object = Feedback.objects.get(id = id)
    feedback_object.delete()
    return redirect('student_view_feedbacks')

def search_books(request):
    form = BookSearchForm()
    books = None
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Add_Book.objects.filter(book_name__icontains=query) | Add_Book.objects.filter(author_name__icontains=query)
    return render(request, 'student_dash/search_book.html', {'form': form, 'books': books})

def issue_book(request):
    form = IssueBookForm()
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            student = form.cleaned_data['student']
            due_date = timezone.now() + timedelta(days=14)  # 2 weeks
            transaction = Transaction.objects.create(book=book, student=student, due_date=due_date)
            book.available_copies -= 1
            book.save()
            return redirect('search_books')
    return render(request, 'student_dash/issue_book.html', {'form': form})

def renew_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    form = RenewBookForm(instance=transaction)
    if request.method == 'POST':
        form = RenewBookForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction.due_date = timezone.now() + timedelta(days=14)  # Extend by 2 weeks
            transaction.save()
            return redirect('library:my_transactions')
    return render(request, 'student_dash/renew_book.html', {'form': form, 'transaction': transaction})

def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    form = ReturnBookForm(instance=transaction)
    if request.method == 'POST':
        form = ReturnBookForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction.return_date = timezone.now()
            transaction.is_returned = True
            transaction.save()
            book = transaction.book
            book.copies += 1
            book.save()

            # Calculate fine if the book is returned late
            if transaction.return_date > transaction.due_date:
                days_late = (transaction.return_date - transaction.due_date).days
                fine_amount = days_late * 10  # Rs. 10 per day late
                Fine.objects.create(transaction=transaction, amount=fine_amount)

            return redirect('library:my_transactions')
    return render(request, 'student_dash/return_book.html', {'form': form, 'transaction': transaction})

def my_transactions(request):
    student = get_object_or_404(Student, user=request.user)
    transactions = Transaction.objects.filter(student=student)
    return render(request, 'student_dash/my_transactions.html', {'transactions': transactions})

def pay_fine(request,fine_id):
    fine = get_object_or_404(Fine, id=fine_id)
    fine.paid = True
    fine.save()
    return redirect('my_transactions')


def pay_fine(request, fine_id):
    fine = get_object_or_404(Fine, id=fine_id)

    if request.method == 'POST':
        if not fine.paid:
            fine.paid = True
            fine.save()
            # Redirect to a success page or the list of fines
            return redirect('my_transactions')

    return render(request, 'student_dash/pay_fine.html', {'fine': fine})










