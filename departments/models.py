from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CoursesOffered(models.Model):
    name = models.CharField(max_length=255)
    departments = models.ForeignKey(Departments, related_name='coursesOffered', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
