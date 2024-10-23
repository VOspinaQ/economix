from django import forms
from .models import Product, PriceAlert

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['name', 'store', 'url', 'target_price']  # Ajusta los nombres a los del modelo

class PriceAlertForm(forms.ModelForm):
    class Meta:
        model = PriceAlert
        fields = ['product', 'current_price']  # También ajusta los nombres aquí
