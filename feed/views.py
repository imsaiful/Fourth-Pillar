from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    message="Hello World"
    return render(request,'feed/index.html',{"message":message})