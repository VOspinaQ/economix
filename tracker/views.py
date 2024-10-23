from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, PriceAlert
from .forms import ProductForm, PriceAlertForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tracker/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    else:
        form = ProductForm()
    return render(request, 'tracker/add_product.html',{'form': form})

def price_alert_list(request):
    alerts = PriceAlert.objects.select_related('product').all()
    return render(request, 'tracker/price_alert_list.html', {'alerts': alerts})

def add_price_alert(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = PriceAlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.product = product
            alert.save()
            return redirect('price_alert_list')
    else: 
        form = PriceAlertForm()
    return render(request, 'tracker/add_price_alert.html', {'form': form, 'product': product})



# Create your views here.
