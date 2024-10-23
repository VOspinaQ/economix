from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Product, PriceAlert

class EconomixAdminSite(AdminSite):
    site_header = 'Administración Economix'
    site_title = 'Economix - Panel de Control'
    index_title = 'Bienvenido al sitio del administrador'

economix_admin_site = EconomixAdminSite(name='economix_admin')   

@admin.register(Product, site=economix_admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'store', 'target_price', 'created_at')  # Cambia 'current_price' por campos válidos de Product
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(PriceAlert, site=economix_admin_site)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ('product', 'current_price', 'alert_date')  # Elimina 'target_price' y 'email'
    search_fields = ('product__name',)  # Corrige 'product_name' a 'product__name'
    list_filter = ('alert_date',)  # Cambia 'created_at' a 'alert_date'


# Register your models here.
