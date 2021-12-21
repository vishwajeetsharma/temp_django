from django.shortcuts import render, redirect
from npjv.models import Shoe
def home(request):
    return render(request, "home.html", {"name": "rohit"})

def about(request):

    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shoes(request):
    if request.method == "POST":
        shoe_name = request.POST['shoe_name']
        price = request.POST['price']
        shoe_colour = request.POST['shoe_colour']
        shoe_description = request.POST['shoe_description']

        shoe = Shoe(shoe_name=shoe_name, price=price, shoe_colour=shoe_colour, shoe_description=shoe_description)
        shoe.save()

        return redirect("/")
    else:
        shoes = Shoe.objects.all()
        # shoes = Shoe.objects.filter(available_now=True)
        return render(request, "contact.html", {"shoe_dict":shoes})

def blog(request, name):
    context={
        "name":name
    }
    return render(request, "blog.html", context)