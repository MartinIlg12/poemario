from django.shortcuts import render,get_object_or_404
from .models import Clasificaciones,Category
# Create your views here.

def about(request):
    clasi= Clasificaciones.objects.all()
    return render(request,"clasificaciones/about.html",{'clasi':clasi})

def category(request, category_id):
    #category= Category.objects.get(id=category_id)
    category=get_object_or_404(Category, id=category_id)
    clasi=Clasificaciones.objects.filter(clasification=category)
    return render(request, "clasificaciones/category.html",{'clasi':clasi})