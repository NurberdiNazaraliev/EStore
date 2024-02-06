from django.contrib import admin

from .models import Gun, Order, OrderGun

# Register your models here.
class OrderGunInline(admin.TabularInline):
    model = OrderGun
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderGunInline]


admin.site.register(Gun)
admin.site.register(Order, OrderAdmin)




