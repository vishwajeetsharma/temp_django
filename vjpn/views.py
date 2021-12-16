from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return render(request, "vjpn/index.html")
