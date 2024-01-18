from django.contrib import admin
from .models import Romances

# Register your models here.
class RomancesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Romances, RomancesAdmin)