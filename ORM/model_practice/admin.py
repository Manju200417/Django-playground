from django.contrib import admin
from .models import Item,Prodect,Customer

# Register your models here.


# admin.site.register(Item)
admin.site.register(Prodect)
admin.site.register(Customer)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('id',)