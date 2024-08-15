from django.db import models

# Create your models here.
class Student(models.Model):
    # Represents a student entity
    name = models.CharField(max_length=100) # The name of the student
     
    def __str__(self) -> str:
        return self.name # Returns the student name for easy identification
    
class Course(models.Model):
    # Represents a course entity
    name = models.CharField(max_length=100) # The name of the course
    students = models.ManyToManyField(
        Student, related_name='courses'
    ) # Links to the students, allowing a course to have many students and a student to be enrolled in many courses.
    
    def __str__(self) -> str:
        return self.name # Returns the coursr name for easy identification 