from django.contrib import admin

from .models import Student, Teacher


class StudentTeacherInline(admin.TabularInline):
    model = Student.teachers.through

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        StudentTeacherInline,
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        StudentTeacherInline,
    ]
    exclude = ["teachers"]