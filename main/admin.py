from django.contrib import admin
from main.models import Student, Course, Enrollment


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", 'full_name', 'password_number', 'pinfl', 'birth_date')
    list_display = ("id", 'full_name')
    search_fields = ("full_name",)
    list_per_page = 20



class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", 'course_code', 'course')
    list_display_links = ("id", 'course_code')
    search_fields = ['course_code']



class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", 'student', 'course', 'period')
    list_display_links = ("id",)



admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)