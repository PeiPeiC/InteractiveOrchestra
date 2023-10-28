from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'webcam_app/home.html')

def violin(request):
    return render(request,'webcam_app/violin.html')