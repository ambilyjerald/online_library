from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Login_view)
admin.site.register(models.Faculty)
admin.site.register(models.Student)
admin.site.register(models.Add_Book)
admin.site.register(models.Feedback)
admin.site.register(models.Transaction)
admin.site.register(models.Fine)

