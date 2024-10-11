from tkinter.font import names

from rest_framework import serializers

from departments.models import Departments, CoursesOffered


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'name']

class CoursesOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesOffered
        fields = ['id', 'name', 'department']
