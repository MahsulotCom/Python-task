from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product, Shop, Category


class ShopTests(APITestCase):
    def setUp(self):
        self.shop = Shop.objects.create(title='Test Shop', description='Test Description',
                                        imageUrl='http://example.com')

    def test_list_shops(self):
        url = reverse('shop-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_shop(self):
        url = reverse('shop-detail', kwargs={'pk': self.shop.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_shop(self):
        data = {'title': 'New Shop', 'description': 'New Description', 'imageUrl': 'http://newexample.com'}
        url = reverse('shop-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProductTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(title='Test Product', description='Test Description', amount=10,
                                              price=20.00)

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {'title': 'New Product', 'description': 'New Description', 'amount': 5, 'price': 15.00}
        url = reverse('product-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CategoryTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category', description='Test Description')

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {'title': 'New Category', 'description': 'New Description'}
        url = reverse('category-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
