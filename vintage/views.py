from django.shortcuts import render,HttpResponse
from.models import Course
# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')
def course(request):
    details=Course.objects.all()
    return render(request,'course.html',{"Course":details})
def dashboard(request):
    return render(request,'dashboard.html')