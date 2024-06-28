from django.shortcuts import render, redirect

from myapp.forms import library_faculty, add_book_form
from myapp.models import Faculty, Add_Book


def read_faculty(request):
    data=Faculty.objects.all()
    return render(request,'staff_dash/staff_details.html',{'facultykey':data})

def del_faculty(request,id):
    data=Faculty.objects.get(id=id)
    data.delete()
    return redirect('staff_detail')

def up_faculty(request,id):
    n=Faculty.objects.get(id=id)
    form= library_faculty(instance=n)
    if request.method=="POST":
        form= library_faculty(request.POST,instance=n)
        if form.is_valid():
            form.save()
            return redirect("faculty_detail")
    return render(request,"staff_dash/staff_update.html",{"form":form})

def add_book(request):
    current_user=request.user
    faculty_object=Faculty.objects.get(user=current_user)
    data=add_book_form()
    if request.method=="POST":
        data=add_book_form(request.POST,request.FILES)
        if data.is_valid():
            product= data.save(commit=False)
            product.seller = faculty_object
            product.save()
            return redirect("book_table")
    return render(request,"staff_dash/add_book.html",{'data':data})

def book_table(request):
    table = Add_Book.objects.all()
    return render(request,'staff_dash/book_details.html',{'data':table})

def delete_book(request,id):
    data = Add_Book.objects.get(id=id)
    data.delete()
    return redirect("book_table")


def book_update(request,id):
    obj = Add_Book.objects.get(pk=id)
    data = add_book_form(instance=obj)
    if request.method=="POST":
        data = add_book_form(request.POST,request.FILES,instance=obj)
        if data.is_valid():
            data.save()
            return redirect('book_table')
    return render(request,"staff_dash/book_update.html",{"data":data})


