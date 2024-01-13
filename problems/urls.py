from django.urls import path
from . import views

urlpatterns = [
    path('problem_list/', views.ProblemList.as_view(), name='problem_list'),
    path('problem/<int:problem_pk>/', views.Problem.as_view(), name='problem'),
]
