from django.urls import path
from . import views
from rest_framework_nested import routers
from .views import ProductViewSet, CollectionViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'collections', CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, r"products", lookup='product')
products_router.register(r'reviews', ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls
