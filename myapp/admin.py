from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Faculty)
admin.site.register(models.Student)
admin.site.register(models.add_book)
