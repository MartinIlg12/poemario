from django.contrib import admin
from .models import Desamores

# Register your models here.
class DesamoresAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Desamores, DesamoresAdmin)