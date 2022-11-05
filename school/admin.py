from django.contrib import admin

from .models import Student, Teacher, StudentTeacher



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']

class StudentTeacherInline(admin.TabularInline):
    model = StudentTeacher
    extra = 3

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentTeacherInline, ]