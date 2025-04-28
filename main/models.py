from django.db import models



"""
maktab - e.maktab
universitet - hemis

AB4418887
"""

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    password_number = models.CharField(max_length=9)
    pinfl = models.CharField(max_length=14)
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name.title()
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = '2.Students'


class Course(models.Model):
    BASIC = 'B'
    INTERMEDIATE = 'I'
    ADVANCED ='A'
    LEVELS = (
        (BASIC, 'Basic'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, "Advanced")
    )

    course_code = models.CharField(max_length=10)
    course = models.CharField(max_length=30)
    level = models.CharField(max_length=1, choices=LEVELS, blank=False, null=False, default=BASIC)
    

    def __str__(self):
        return self.course
    


    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = '1.Courses'

class Enrollment(models.Model):
    MORNING = 'M'
    AFTERNOON = 'A'
    NIGHLY = 'N'
    ONLINE = 'O'
    PERIODS = (
        (MORNING, 'Morning'),
        (AFTERNOON, 'Afternoon'),
        (NIGHLY, 'Nightly'),
        (ONLINE, "Online")
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIODS, blank=False, null=False, default=AFTERNOON)


    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = '3.Enrollment'