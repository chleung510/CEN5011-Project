from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request, "Main page.html")

def Add(request):
    try:
        x=int(request.GET['email'])
        y=int(request.GET['password'])
        z = x+y
        return HttpResponse("<html><body bgcolor=yellow><h1>Sum is:"+str(z)+"<h1></body></html>")
    except(ValueError):
        return HttpResponse("Invalid Input")

def index(request):
    return render(request, "Main page.html")