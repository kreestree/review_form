from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.ReportProblem.as_view(), name='add_problem'),
    path('report/success/', views.success, name='success'),
    path('ajax/load-equipments/', views.load_equipments, name='ajax_load_equipments'),  # AJAX dropdown list options
]
