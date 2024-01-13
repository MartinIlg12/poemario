from django.shortcuts import render
from .models import Amores

# Create your views here.

def amor(request):
    amores = Amores.objects.all()
    return render(request,"amores/amor.html", {'amores':amores})
