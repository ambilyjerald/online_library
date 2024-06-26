from django.shortcuts import render, redirect

from myapp.forms import library_faculty
from myapp.models import Faculty


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
