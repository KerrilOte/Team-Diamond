from django.http import HttpResponse

def home_page(request):
    return  HttpResponse("<h1> Hello Team Diamond.</h1>")