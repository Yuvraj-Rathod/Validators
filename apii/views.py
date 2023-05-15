from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_get(request):
    
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parser(stream)
            id = python_data.get('id', None)
            if id is not None:
                stu = Student.objets.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer)
        return HttpResponse(json_data, content_type = 'application/json')
stu = Student.objects.all()
serializer = StudentSerializer(stu, many = True)
json_data = JSONRenderer().render(serializer.data)
# return HttpResponse(json_data, content_type = 'application/json')
                    
if request.method == 'POST':
    json_data = request.body        
    stream = io.BytesIO()
    python_data = JSONParser().parser(stream)
    serializer = StudentSerializer(data=python_data)
if serializer.is_valid():
         serializer.save()
         res = {'msg': 'data created'}
         json_data = JSONRenderer().render(serializer.errors)
         return HttpResponse(json_data, content_type = 'application/json')

