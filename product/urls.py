from django.urls import path
from .views import (
    product_delete_view,
    product_detail_view,
    product_create_view,
    product_list_view,
)

app_name = 'product'
urlpatterns = [

    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-list'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/delete', product_delete_view, name='product-delete'),

    ]

