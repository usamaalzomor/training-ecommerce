from django.urls import path
from . import views
from rest_framework_nested import routers
from .views import CustomerViewSet, OrderViewSet, ProductImageViewSet, ProductViewSet, CollectionViewSet, ReviewViewSet, CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'collections', CollectionViewSet)
router.register(r'carts', CartViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, r"products", lookup='product')
products_router.register(r'reviews', ReviewViewSet, basename='product-reviews')
products_router.register(r'images', ProductImageViewSet, basename='product-image')

items_router = routers.NestedDefaultRouter(router, r"carts", lookup='cart')
items_router.register(r'items', CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + products_router.urls + items_router.urls
