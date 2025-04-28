from rest_framework import serializers
from main.models import Student, Course, Enrollment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'password_number', 'pinfl', 'birth_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"



class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class ListStudentEnrollmentSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField()
    period = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['courses', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    

class ListCourseStudentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.full_name')


    class Meta:
        model = Enrollment
        fields = ['student_name']