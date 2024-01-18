
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('categorias/', views.categorias, name="categorias"),
    path('contacto/', views.contacto, name="contacto"),
]