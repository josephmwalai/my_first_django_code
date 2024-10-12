from django.urls import path

from departments.views import DepartmentListView, CoursesOfferedView, DepartmentCreateView, CreateCourseView

urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('coursesOffered/<int:department_id>/', CoursesOfferedView.as_view()),
    path('createDepartment/', DepartmentCreateView.as_view()),
    path('createCourse/', CreateCourseView.as_view())
]