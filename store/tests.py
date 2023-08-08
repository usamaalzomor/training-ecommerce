from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Cart, Product, Collection

class CartViewSetTestCase(APITestCase):
    def setUp(self):
        # Assuming you have a Product model related to your Cart.
        collection = Collection.objects.create(title='Test Collection')
        self.product = Product.objects.create(title='Test Product', unit_price=100.0, inventory = 1, collection=collection)


    def test_create_cart(self):
        response = self.client.post('/store/carts/', {})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 1)


    def test_retrieve_cart(self):
        # Create a Cart object for testing retrieve operation.
        cart = Cart.objects.create()
        response = self.client.get(f'/store/carts/{cart.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_destroy_cart(self):
        # Create a Cart object for testing destroy operation.
        cart = Cart.objects.create()
        self.assertEqual(Cart.objects.count(), 2)
        response = self.client.delete(f'/store/carts/{cart.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cart.objects.count(), 0)
