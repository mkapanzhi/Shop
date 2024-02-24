from django.urls import path

from .views import get_store_page, get_add_product_page, get_description_page, get_product_from_store

urlpatterns = [
    path('', get_store_page, name='home'),
    path('add_product/', get_add_product_page, name='add_product'),
    path('desc/<int:id>/', get_description_page, name='desc'),
    path('get_product_from_store/<int:id>', get_product_from_store, name='get_product_from_store')
]
