from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_django(request):
 return HttpResponse('Hello Django')

def hello_html(request):
 return HttpResponse('<h1>Hello Python</h1>')

def html_var(request):
 a = '<h1>Hello variable</h1>'
 return HttpResponse(a)

def html_math(request):
 a = 10 + 10
 return HttpResponse(a)

def html_format(request):
 a = 'CoodingWorld'
 return HttpResponse(f'Hello How are You {a}') 

def index(request):
 return HttpResponse ('Home Page')