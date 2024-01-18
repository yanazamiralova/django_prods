from django.shortcuts import render, redirect
from .models import Orders, Products, Customers
from .forms import OrderForm, ProdForm, CustForm


def index(request):
    orders_all = Orders.objects.all()
    return render(request, 'myapp/index.html', {'orders_all': orders_all})


def order_form(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = OrderForm()
    context = {'form': form, 'error': error}
    return render(request, 'myapp/order_form.html', context)


def clients(request):
    client = Customers.objects.all()
    return render(request, 'myapp/clients.html', {'client': client})


def products(request):
    prod = Products.objects.all()
    return render(request, 'myapp/products.html', {'prod': prod})


def orders(request):
    order = Orders.objects.all()
    return render(request, 'myapp/products.html', {'order': order})


def prod_form(request):
    error = ''
    if request.method == 'POST':
        form = ProdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ProdForm()
    context = {'form': form, 'error': error}
    return render(request, 'myapp/prod_form.html', context)


def cust_form(request):
    error = ''
    if request.method == 'POST':
        form = CustForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = CustForm()
    context = {'form': form, 'error': error}
    return render(request, 'myapp/cust_form.html', context)

