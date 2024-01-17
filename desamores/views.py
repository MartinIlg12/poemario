from django.shortcuts import render
from .models import Desamores

# Create your views here.

def desamor(request):
    desamores = Desamores.objects.all()
    return render(request,"desamores/desamor.html", {'desamores':desamores})
