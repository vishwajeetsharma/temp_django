from django.shortcuts import render, HttpResponse

def index(reuquest):
    return HttpResponse(''' <h1> Hello, World!! Index </h1><a href="/about">click here</a> ''')

def about(request):
    return HttpResponse(''' <h1> Hello, World!! About </h1><a href="/">click here</a> ''')