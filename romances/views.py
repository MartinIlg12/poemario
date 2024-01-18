from django.shortcuts import render
from .models import Romances

# Create your views here.
def romance(request):
    romances = Romances.objects.all()
    return render(request,"romances/romance.html", {'romances':romances})