from django.contrib import admin
from .models import Amores


# Register your models here.
class AmoresAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(Amores, AmoresAdmin)