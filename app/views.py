from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def studentform(request):
    SFO=student()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=student(request.POST)
        if SFDO.is_valid():
           return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('data not inserted')
    
    return render(request,'studentform.html',d)
