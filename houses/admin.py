from django.contrib import admin
from .models import House, Entrance, Apartment

class EntranceAdmin(admin.ModelAdmin):
    filter_horizontal = ('guards',)

admin.site.register(House)
admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Apartment)