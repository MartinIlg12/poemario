
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name="about"),
    path('category/<int:category_id>/', views.category,name="category"),
]