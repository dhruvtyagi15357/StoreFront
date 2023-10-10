from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
def sayhello(req):
    x = 1
    y = x**2
    return render(req, 'hello.html')

def sayhello2(req):
    return render(req, 'hello2.html', {'name':'John'})

