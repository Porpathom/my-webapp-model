from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def index(request):
    
    context = {}
    
    students = models.Student.objects.all().order_by("id") 
    
    context['students'] = students
    
    # context = {
    #     'students' : students
    # }
    
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def studentdetail(request, id):
    context = {}
    student = models.Student.objects.get(id=id)
    context['student'] = student
    return render(request, 'detail.html')