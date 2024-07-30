from django.contrib import admin
from .models import House, Entrance, Apartment, CustomUser
from django.contrib.auth.admin import UserAdmin


class EntranceAdmin(admin.ModelAdmin):
    filter_horizontal = ("guards",)


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("role",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("role",)}),)


admin.site.register(House)
admin.site.register(Entrance, EntranceAdmin)
admin.site.register(Apartment)
admin.site.register(CustomUser, CustomUserAdmin)
