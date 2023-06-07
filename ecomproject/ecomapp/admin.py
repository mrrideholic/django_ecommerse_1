from django.contrib import admin
from .models import Category, Product


# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, categoryAdmin)


class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock', 'desc', 'available', 'created', 'updated']
    list_editable = ['available', 'price','stock']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, productAdmin)
