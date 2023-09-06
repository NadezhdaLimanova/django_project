from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'price')
    if sort == 'min_price':
        phones_all = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones_all = reversed(Phone.objects.all().order_by('price'))
    elif sort == 'name':
        phones_all = Phone.objects.all().order_by('name')
    else:
        phones_all = Phone.objects.all()
    context = {'phones': phones_all,
               'sort': sort}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
