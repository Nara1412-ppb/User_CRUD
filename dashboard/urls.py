from django.urls import path
from .views import CreateEmployee,EmployeeDetails,UpdateEmployee
urlpatterns = [
    path('Create/',CreateEmployee.as_view()),
    path('Search/',EmployeeDetails.as_view()),
    path('Update/',UpdateEmployee.as_view()),
    path('Delete/',UpdateEmployee.as_view())
]