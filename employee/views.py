from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
import jsonpickle

from .forms import EmployeeForm

jsonpickle.set_encoder_options('simplejson', indent=8)

# Create your views here.
class EmployeeListView(View):
    template_name = "employee_list.html"
    queryset = Employee.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'employee_list': self.get_queryset()}
        # print(self.get_queryset()[0].department.name)
        return render(request, self.template_name, context)

class EmployeeObjectMixin(object):
    model = Employee
    lookup = 'pk'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj        

class EmployeeListAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Employee.objects.all()

        data = [{
            "name": employee.name,
            "email": employee.email,
            "department": employee.get_department_name()
        } for employee in queryset]

        json = jsonpickle.encode(data)
        return Response(data)

class EmployeeDeleteAPI(EmployeeObjectMixin, APIView):
    def delete(self, request, pk=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = {{
                "name": employee.name,
                "email": employee.email,
                "department": employee.get_department_name()
            } for employee in obj}
            context['success'] = True
            obj.delete()
            json = jsonpickle.encode(context)
            return Response(json)
        return Response(jsonpickle.encode({"success": False}))

class EmployeeCreateAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = EmployeeForm(request.POST)        
        context = {"success": False}

        if form.is_valid():
            context = {"success": True, "form": form.cleaned_data}
            form.save()

        return Response(jsonpickle.encode(context))
