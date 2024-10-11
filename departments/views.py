from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from departments.models import Departments, CoursesOffered
from departments.serializers import DepartmentsSerializer, CoursesOfferedSerializer


# Create your views here.
class DepartmentListView(APIView):
    def get(self, request,*args, **kwargs):
        departments = Departments.objects.all()
        serializer = DepartmentsSerializer(departments, many=True)
        return Response(serializer.data)

class CoursesOfferedView(APIView):
    def get(self, request, department_name):
        courses = CoursesOffered.objects.filter(department_name=department_name)
        serializer = CoursesOfferedSerializer(courses, many=True)
        return Response(serializer.data)

class DepartmentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

