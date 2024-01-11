from django.shortcuts import render
from .models import Service
# Create your views here.
def poemas(request):
    services = Service.objects.all()
    return render(request,"services/poemas.html", {'services':services})