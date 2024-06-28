from django.shortcuts import redirect, render

from myapp.forms import add_book_form
from myapp.models import Faculty, Add_Book


def admin_book_table(request):
    table = Add_Book.objects.all()
    return render(request,'admin_dash/book_details.html',{'data':table})

def admin_delete_book(request,id):
    data = Add_Book.objects.get(id=id)
    data.delete()
    return redirect("book_table")

