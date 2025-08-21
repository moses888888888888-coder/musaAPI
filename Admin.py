from django.contrib import admin
from .models import Subject, Grade, Teacher, TeachingAssignment

admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Teacher)
admin.site.register(TeachingAssignment)
