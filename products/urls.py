from django.urls import path
from products.views import (
    # product_list_view,
    ProductListView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    ProductDetailSlugView)


urlpatterns = [
    path('', ProductListView.as_view(), name="productList"),
    path('<slug>', ProductDetailSlugView.as_view(), name="productDetail"),
]
