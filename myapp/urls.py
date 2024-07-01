from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from myapp import views, staff_views, admin_views

urlpatterns = [

     path("",views.home,name='home'),
     path('dashboard',views.dashboard,name='dashboard'),
     path('loginpage',views.loginpage,name='loginpage'),

     path('regfaculty',views.reg_faculty,name='regfaculty'),
     path('regstudent',views.reg_student,name='regstudent'),

     path('admindash',views.admindash,name='admindash'),
     path('facultydash',views.facultydash,name='facultydash'),
     path('studentdash',views.studentdash,name='studentdash'),


     path('faculty_detail',staff_views.read_faculty,name='faculty_detail'),
     path("faculty_del/<int:id>/",staff_views.del_faculty,name='faculty_del'),
     path("faculty_up/<int:id>/",staff_views.up_faculty,name='faculty_up'),
     path("logout/", views.logout_view, name="logout"),

     path('addbook',staff_views.add_book,name='addbook'),
     path("book_table",staff_views.book_table,name='book_table'),
     path("book_delete/<int:id>/",staff_views.delete_book,name="book_delete"),
     path("book_update/<int:id>/",staff_views.book_update,name="book_update"),

     path("admin_book_table",admin_views.admin_book_table,name='admin_book_table'),
     path("admin_book_delete/<int:id>/",admin_views.admin_delete_book,name="admin_book_delete"),

     path('admin_view_feedbacks/', admin_views.admin_view_feedbacks, name='admin_view_feedbacks'),
     path('admin_feedback_reply/<int:id>/', admin_views.admin_feedback_reply, name='admin_feedback_reply'),

     path('faculty_approval_requests/', admin_views.faculty_approval_requests, name='faculty_approval_requests'),
     path('remove_faculty_request/<int:id>/', admin_views.remove_faculty_request, name='remove_faculty_request'),
     path('approve_faculty/<int:id>/', admin_views.approve_faculty, name='approve_faculty'),

     path('student_approval_requests/', admin_views.student_approval_requests, name='student_approval_requests'),
     path('remove_student_request/<int:id>/', admin_views.remove_student_request, name='remove_student_request'),
     path('approve_student/<int:id>/', admin_views.approve_student, name='approve_student'),



]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
