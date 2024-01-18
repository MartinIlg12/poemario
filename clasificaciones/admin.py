from django.contrib import admin
from .models import Category, Clasificaciones

# Register your models here.
class  CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category, CategoryAdmin)

class ClasificacionesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Clasificaciones,ClasificacionesAdmin)