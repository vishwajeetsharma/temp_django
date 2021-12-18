from django.shortcuts import render
from npjv.models import Shoe
def home(request):
    return render(request, "home.html", {"name": "rohit"})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shoes(request):
    shoe = Shoe.objects.get(shoe_colour="lime")
    shoe_dict = {
        "shoe_name": shoe.shoe_name,
        "price": shoe.price
    }
    return render(request, "contact.html", shoe_dict)