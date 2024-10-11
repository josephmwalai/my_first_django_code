from django.urls import path
from comrades.views import ComradesListView, ComradesDetailView, ComradesCreateView

urlpatterns = [
    path('comradesList', ComradesListView.as_view()),
    path('comradesDetails', ComradesDetailView.as_view()),
    path('createComrade', ComradesCreateView.as_view())
]