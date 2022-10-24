from django.urls import path
from .views import *

app_name = 'department'
urlpatterns = [
    path('', DepartmentListAPI.as_view(), name='department-list-api'),
    path('create/', DepartmentCreateAPI.as_view(), name='department-create-api'),
    path('<int:pk>/delete/', DepartmentDeleteAPI.as_view(), name='department-delete-api'),
]