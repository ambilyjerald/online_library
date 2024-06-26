from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from myapp import views, staff_views

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
     path("logout/", views.logout_view, name="logout")
]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
