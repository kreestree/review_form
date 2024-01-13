from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.ReportProblem.as_view(), name='add_problem'),
    path('report/success/', views.success, name='success'),
]

