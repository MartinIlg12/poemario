from django.contrib import admin
from .models import Category, Clasificaciones

# Register your models here.
class  CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category, CategoryAdmin)

class ClasificacionesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','created')
    search_fields=('title','author__username','clasification__name')
    date_hierarchy='created'
    list_filter=('author__username','clasification__name')
admin.site.register(Clasificaciones,ClasificacionesAdmin)