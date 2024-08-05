from django.contrib import admin

# Register your models here.
from .models import Product


admin.site.site_header = "Admin toys shop"
admin.site.site_title = " Site django admin"
admin.site.index_title = "My admin panel"


class ProductAdmin(admin.ModelAdmin):
    list_display =("id", "name", "price", "description", "image", "seller_id")
    search_fields = ("name",)
    list_editable =("name", "price", "description", "image",)
    actions = ("make_zero",)
 
    def make_zero(self, request, queryset):
        queryset.update(price=0)
        

admin.site.register(Product, ProductAdmin)
