from django.urls import path
from .import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product,name= 'add_product'),
    path('alerts/', views.price_alert_list, name='price_alert_list'),
    path('alerts/add/<int:product_id>/', views.add_price_alert, name='add_price_alert'),
         
]