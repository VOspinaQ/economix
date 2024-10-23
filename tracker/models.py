from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name= "Nombre del producto")
    store = models.CharField(
        max_length=50, 
        choices=[('AliExpress', 'Aliexpress'), ('Walmart', 'Walmart')], 
        verbose_name="Tienda",
        default='AliExpress'  # Valor predeterminado para las filas existentes
    )
    url = models.URLField(verbose_name="Enlace del producto")
    target_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio objetivo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creación")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name} - {self.store}"
    

class PriceAlert(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="alerts")
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio actual", default=0.00)
    alert_date = models.DateTimeField(default=timezone.now, verbose_name="Fecha de la alerta")

    class Meta: 
        verbose_name = "Alerta de Precio"
        verbose_name_plural = "Alerta de Precios"

    def __str__(self):
        return f"Alerta para {self.product.name} - Precio actual: {self.current_price}"
