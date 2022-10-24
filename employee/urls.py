from django.urls import path
from .views import *

app_name = 'employee'
urlpatterns = [
    path('', EmployeeListAPI.as_view(), name='employee-list-api'),
    path('create/', EmployeeCreateAPI.as_view(), name='employee-create-api'),
    path('<int:pk>/delete/', EmployeeDeleteAPI.as_view(), name='employee-delete-api'),
]