from django.http import HttpResponse

def index(reuquest):
    return HttpResponse(''' <h1> Hello, World!! </h1><br><a href="facebook.com">click here</a> ''')