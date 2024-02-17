from django.shortcuts import render
from django.http import HttpResponse
from .models import New
# Create your views here.

def demo(request):
    obj=New.objects.all()

    return render(request,"index.html",{'result':obj})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     div=x/y
#     multy=x*y
#     return render(request,"result.html",{'obj':add,'res':sub,'res2':div,'res3':multy})


