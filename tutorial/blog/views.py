from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Bienvenido a mi Blog")
    return render(request, "blog/home.html")

