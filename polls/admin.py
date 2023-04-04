from django.contrib import admin
from polls.models import Ecole


class EcoleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'location'
    )


# Register your models here.
admin.site.register(Ecole, EcoleAdmin)
