from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def index(request):
    
    context = {}
    
    students = models.Student.objects.all().order_by("id") 
    
    for student in students:
        student.prefix_str = getmodelschoice(
            student.prefix, models.prefix_choices
        )
    
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
    # student = models.Student.objects.get(id=id) 
    students = models.Student.objects.filter(id=id)
    for student in students:
        student.prefix_str = getmodelschoice(
            student.prefix, models.prefix_choices
        )
        context['student'] = student
    return render(request, 'detail.html',context)

def getmodelschoice(num, choices):
    for choice in choices:
        if choice[0] == num:
                return choice[1]
