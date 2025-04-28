from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main import views



router = routers.DefaultRouter()


router.register('students', views.StudentViewSet, basename='Students')
router.register('courses', views.CourseViewSet, basename='Courses')
router.register('enrollment', views.EnrollmentViewSet, basename='Enrollments')

urlpatterns = [
    # API
    path("", include(router.urls)),
    path("course/<int:pk>/enrollments", views.ListCourseStudents.as_view()),
    path("student/<int:pk>/enrollments", views.ListStudentEnrollments.as_view()),

    #Django admin
    path('admin/', admin.site.urls),

]
