from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<int:product_id>', views.product, name="product"),
    # path('product/(?P<product_id>\w+)/', views.product, name='product'),
    # re_path(r'^(?P<product_id>[0-9])/$', views.product, name='product'),

]

