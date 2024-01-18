from django.shortcuts import render
from .models import Clasificaciones

# Create your views here.

def about(request):
    clasificaciones = Clasificaciones.objects.all()
    return render(request,"clasificaciones/about.html",{'clasificaciones':clasificaciones})