from django.shortcuts import render
from .forms import SubscriberFrom
from products.models import *

# Create your views here.

def landing(request):
    form = SubscriberFrom(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, "pages/index.html", locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, "pages/home.html", locals())
