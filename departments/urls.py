from django.urls import path

from departments.views import DepartmentListView, CoursesOfferedView, DepartmentCreateView

urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('coursesOffered/<str:department_name>/', CoursesOfferedView.as_view()),
    path('createDepartment/', DepartmentCreateView.as_view())
]