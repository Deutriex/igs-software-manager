from django.shortcuts import get_object_or_404, render

from department.forms import DepartmentForm
from .models import Department
from employee.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
import jsonpickle


# Create your views here.

class DepartmentObjectMixin(object):
    model = Department
    lookup = 'pk'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj    

class DepartmentListAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Department.objects.all()

        data = [{
            "id": department.id,
            "name": department.name
        } for department in queryset]

        json = jsonpickle.encode(data)
        print(json)
        return Response(data)

class DepartmentCreateAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = DepartmentForm(request.POST)        
        context = {}

        if form.is_valid():
            context = {"form": form.cleaned_data, "success": True}
            form.save()
        else:
            context = {"success": False}

        return Response(jsonpickle.encode(context))

class DepartmentDeleteAPI(DepartmentObjectMixin, APIView):
    def delete(self, request, pk=None, *args, **kwargs):
        context = {"success": False}
        obj = self.get_object()
        if obj is not None:
            has_employees = Employee.objects.filter(department=self.kwargs.get('pk')).count()
            
            print("has_employees: " + str(has_employees))
            print(obj)

            context['object'] = {
                "name": obj.name
            }

            if has_employees == 0:
                context['success'] = True
                obj.delete()

            json = jsonpickle.encode(context)
            return Response(json)
        return Response(jsonpickle.encode(context))