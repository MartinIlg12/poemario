"""
URL configuration for poemario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('categorias/', views.categorias, name="categorias"),
    path('contacto/', views.contacto, name="contacto"),
    path('poemas/', views.poemas, name="poemas"),
    path('amor/', views.amor, name="amor"),
    path('desamor/', views.desamor, name="desamor"),
    path('romance/', views.romance, name="romance"),
    path('admin/', admin.site.urls),
]
