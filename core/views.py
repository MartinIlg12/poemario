from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def categorias(request):
    return render(request,"core/categorias.html")

def contacto(request):
    return render(request,"core/contacto.html")

def poemas(request):
    return render(request,"core/poemas.html")

def amor(request):
    return render(request,"core/amor.html")

def desamor(request):
    return render(request,"core/desamor.html")

def romance(request):
    return render(request,"core/romance.html")